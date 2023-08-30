from django.shortcuts import render
from .forms import signUpForm
from django.views.generic import CreateView,ListView



class signUp(CreateView):
    form_class=signUpForm
    template_name='authentication/signup.html'
    context_object_name='form'
    success_url='/'

def home(request):
    return render(request,'home.html')



