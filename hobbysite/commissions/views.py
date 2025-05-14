from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from .models import Commission, JobApplication, Job
from .forms import CommissionForm
from user_management.models import Profile


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/list.html"

    def get_context_data(self, **kwargs):
        ctx = super(CommissionListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            curr_user = Profile.objects.get(user=self.request.user)
            ctx["commissions_placed"] = Commission.objects.filter(
                author=curr_user
            )
            ctx["commissions_applied"] = JobApplication.objects.filter(
                applicant=curr_user
            )
        return ctx


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/detail.html"

    def get_context_data(self, **kwargs):
        ctx = super(CommissionDetailView, self).get_context_data(**kwargs)
        ctx["manpower_sum"] = 0
        ctx["manpower_open"] = 0

    def post(self, request, *args, **kwargs):
        curr_commission = Commission.objects.get(pk=self.kwargs["pk"])
        curr_user = Profile.objects.get(user=self.request.user)

        form = JobApplication()
        form.job = Job.objects.get(commission=curr_commission)
        form.applicant = Profile.objects.get(user=curr_user)
        form.save()

        return redirect("commissions:detail", pk=self.kwargs["pk"])


class CommissionCreateView(CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commissions/update_create.html"

    def get_context_data(self, **kwargs):
        ctx = super(CommissionCreateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Create a Commission'
        ctx['header'] = 'Create a Commission'
        ctx['button_text'] = 'Publish Commission'
        return ctx


class CommissionUpdateView(UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commissions/update_create.html"

    def get_context_data(self, **kwargs):
        ctx = super(CommissionUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Update Commission'
        ctx['header'] = 'Update Commission'
        ctx['button_text'] = 'Update'
        return ctx
