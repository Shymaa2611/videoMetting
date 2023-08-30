from django.shortcuts import render,redirect
from .forms import signUpForm
from django.contrib.auth import login,logout,authenticate


def signUp(request):
    if request.method=='POST':
        form=signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form=signUpForm()
    return render(request,'authentication/signup.html') 
def user_login(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = form.save()  
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                return render(request, 'authentication/login.html', {"message": "Invalid credentials"})
    else:
        form=signUpForm()
    
    return render(request, 'authentication/login.html',{"form":form})


def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dasboard.html')



