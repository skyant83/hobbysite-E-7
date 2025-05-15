from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Commission, JobApplication, Job
from .forms import CommissionForm, JobFormSet
from user_management.models import Profile


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/list.html"

    def get_context_data(self, **kwargs):
        ctx = super(CommissionListView, self).get_context_data(**kwargs)
        commission_choices = ['open', 'full', 'complete', 'discontinued']

        if self.request.user.is_authenticated:
            curr_user = Profile.objects.get(user=self.request.user)

            ctx["commission_list"] = ChoiceSort(
                commission_choices,
                Commission.objects.all())

            ctx["commissions_placed"] = ChoiceSort(
                commission_choices,
                Commission.objects.filter(author=curr_user))

            ctx["commissions_applied"] = ChoiceSort(
                commission_choices,
                JobApplication.objects.filter(applicant=curr_user))

        return ctx


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/detail.html"

    def get_context_data(self, **kwargs):
        current_commission = Commission.objects.get(pk=self.kwargs['pk'])
        ctx = super(CommissionDetailView, self).get_context_data(**kwargs)
        ctx['pk'] = self.kwargs['pk']
        ctx['jobs'] = Job.objects.filter(commission=current_commission)

        jobs_applications = {}
        for job in ctx['jobs']:
            no_pos_filled = (
                JobApplication.objects.filter(job=job) &
                JobApplication.objects.filter(status='accepted')
            ).__len__()

            if job.manpower_required == no_pos_filled:
                job.status = 'full'
                job.save()

            jobs_applications[job] = no_pos_filled

        job_listing = (ctx['jobs'] & Job.objects.filter(status='full')).__len__()
        if job_listing == ctx['jobs'].__len__():
            current_commission.status = 'full'
            current_commission.save()

        ctx['applications'] = jobs_applications
        return ctx

    def post(self, request, *args, **kwargs):
        curr_commission = Commission.objects.get(pk=self.kwargs["pk"])
        curr_user = Profile.objects.get(user=self.request.user)

        for job in Job.objects.filter(commission=curr_commission):
            some_key = request.POST.get(job.role, None)
            if some_key is not None:
                JobApplication.objects.create(
                    job=job,
                    applicant=curr_user,
                    status='pending'
                )

        return redirect("commissions:detail", pk=self.kwargs["pk"])


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commissions/update_create.html"

    def post(self, request, *args, **kwargs):
        commission_form = CommissionForm(request.POST)
        job_set = JobFormSet(request.POST)

        if commission_form.is_valid() and job_set.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = Profile.objects.get(user=self.request.user)
            commission.save()

            jobs = job_set.save(commit=False)
            for job in jobs:
                job.commission = commission
                job.save()

            return redirect('commissions:detail', pk=commission.pk)

        self.object_list = self.get_queryset(**kwargs)
        ctx = self.get_context_data(**kwargs)
        return self.render_to_response(ctx)

    def get_context_data(self, **kwargs):
        ctx = super(CommissionCreateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Create a Commission'
        ctx['header'] = 'Create a Commission'
        ctx['button_text'] = 'Publish Commission'
        ctx['commission_form'] = CommissionForm()
        ctx['job_form'] = JobFormSet()
        return ctx


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commissions/update_create.html"

    def post(self, request, *args, **kwargs):
        curr_commission = Commission.objects.get(pk=self.kwargs['pk'])
        commission_form = CommissionForm(
            request.POST, instance=curr_commission)
        job_set = JobFormSet(
            request.POST, instance=curr_commission)

        if commission_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = Profile.objects.get(user=self.request.user)
            commission.save()

        if job_set.is_valid():
            jobs = job_set.save(commit=False)
            for job in jobs:
                job.commission = commission
                job.save()

        return redirect('commissions:detail', pk=commission.pk)

    def get_context_data(self, **kwargs):
        curr_commission = Commission.objects.get(pk=self.kwargs['pk'])
        ctx = super(CommissionUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Update Commission'
        ctx['header'] = 'Update Commission'
        ctx['button_text'] = 'Update'

        ctx['commission_form'] = CommissionForm(instance=curr_commission)
        if self.request.POST:
            ctx['job_form'] = JobFormSet(
                self.request.POST,
                instance=self.object
            )
        else:
            ctx['job_form'] = JobFormSet(instance=self.object)

        return ctx


def ChoiceSort(Choices, ToBeSorted):
    output = []

    for choice in Choices:
        for entry in ToBeSorted:
            if entry.status == choice:
                output.append(entry)

    return output
