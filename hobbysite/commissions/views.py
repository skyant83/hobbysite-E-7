from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

class CommissionListView(ListView):
    model = Commission
    template_name = "comm/comm_list.html"

class CommissionDetailView():
    model = Commission
    template_name = "comm/comm_details.html"