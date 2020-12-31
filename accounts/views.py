from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.


def login(request):
    #Login the user
    if request.method == "POST":
        return
    else:
        return render(request,'accounts/login.html')

def logout(request):
    return redirect('index')

def register(request):
    #Register the user
    if request.method == "POST":
        messages.error(request,"Testing Error message")
        return redirect('register')
    else:
        return render(request,'accounts/register.html')



    return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')