from django.shortcuts import render,redirect
from .forms import signUpForm
from django.contrib.auth.models import User

def signUp(request):
    if request.method=='POST':
        form=signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=signUpForm()
    return render(request,'authentication/signup.html',{'form':form}) 


def login(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                return redirect('home')
            else:
                return redirect('signUp')
    else:
        form =signUpForm()
    context = {'form': form}
    return render(request, 'authentication/login.html', context)


def home(request):
    return render(request,'pages/home.html')

def dashboard(request):
    return render(request,'pages/dasboard.html')


def meeting(request):
    return render(request,'pages/meeting.html')


