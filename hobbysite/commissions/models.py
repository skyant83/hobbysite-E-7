from django.urls import reverse
from django.db import models
from user_management.models import Profile


class Commission(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="commissions"
    )
    description = models.TextField()
    status = models.CharField(
        choices=["Open", "Full", "Completed", "Discontinued"],
        default="Open"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ["created_on"]


class Job(models.Model):
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="job"
    )
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
    status = models.CharField(
        choices=["Open", "Full"],
        default="Open"
    )

    class Meta:
        ordering = ["status"]


class JobApplication(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="application"
    )
    applicant = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="application"
    )
    status = models.CharField(
        choices=["Pending", "Accepted", "Rejected"],
        default="Pending"
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "applied_on"]
