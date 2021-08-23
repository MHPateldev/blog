from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView

class HomeView(TemplateView):
    template_name="index.html"

class TextView(TemplateView):
    template_name="text.html"

class ThanksView(TemplateView):
    template_name="thanks.html"