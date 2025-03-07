from django.shortcuts import render

from django.http import HttpResponse

class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/comm-list.html"

class CommissionDetailView():
    model = Commission
    template_name = "commissions/comm-details.html"