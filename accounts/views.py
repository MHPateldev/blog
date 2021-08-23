from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from accounts.forms import UserForm
# Create your views here.

def index(request):
    return HttpResponse("Hello")

class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("home")
    template_name = "accounts/signup.html"
