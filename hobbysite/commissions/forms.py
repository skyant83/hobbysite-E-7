from django import forms
from .models import Commission, Job


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ["title", "description", "status"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']


JobFormSet = forms.inlineformset_factory(
    Commission,
    Job,
    form=JobForm,
    extra=3,
    can_delete=True,
    fields=['role', 'manpower_required', 'status']
)
