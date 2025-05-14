from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .models import Profile
from .forms import RegistrationForm


# Create your views here.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name']
    template_name = 'user_management/profile_detail.html'


class ProfileCreateView(FormView):
    template_name = 'user_management/profile_create.html'
    form_class = RegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistrationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user,
                              display_name=form.cleaned_data['display_name'],
                              email_address=user.email)
            profile.save()
            return redirect('user_management:profile_update', pk=user.pk)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
