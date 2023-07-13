from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.views import generic
from django.http import HttpResponse

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account_login')

def home(request):
    return HttpResponse('200')