from django.urls import reverse
from django.db import models
from user_management.models import Profile


class Commission(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='commissions'
    )
    description = models.TextField()
    status = models.CharField(
        choices={
            'open': 'Open',
            'full': 'Full',
            'complete': 'Completed',
            'discontinued': 'Discontinued'
        },
        default='open',
        max_length=255
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['created_on']


class Job(models.Model):
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name='job'
    )
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
    # manpower_accepted = models.IntegerField()
    status = models.CharField(
        choices={
            'open': 'Open',
            'full': 'Full',
        },
        default='open',
        max_length=255
    )

    def __str__(self):
        return self.role

    class Meta:
        ordering = ['-status']


class JobApplication(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='application'
    )
    applicant = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='application'
    )
    status = models.CharField(
        choices={
            'pending': 'Pending',
            'accepted': 'Accepted',
            'rejected': 'Rejected'
        },
        default='pending',
        max_length=255
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job + ' ' + self.applicant

    class Meta:
        ordering = ['applied_on']
