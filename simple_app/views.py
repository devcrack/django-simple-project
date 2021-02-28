from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class FirstPageView(TemplateView):
    template_name = "page-1.html"
