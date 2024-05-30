from django.shortcuts import render
from django.http import HttpResponse
from .models  import Perfume
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# Create your views here.
def home(request):
  perfumes = Perfume.objects.all()  # Use plural for multiple perfumes
  context = {'perfumes': perfumes}  # Use correct dictionary key
  return render(request, 'home.html', context)

def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    Password = request.POST['password']
    user = authenticate(request, username=username, password= Password)
    if user is not None:
      login(request,user)
      messages.success(request,'You have been login')
      return redirect('home')
    else:
      messages.success(request,'fail login')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logout_user(request):
  logout(request)
  messages.success(request,'you have been logout')
  return redirect('home')  # Redirect to the home page or any other page

  #pass

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
      form =SignUpForm(request.POST)
      if form.is_valid():
        form.save()
        username= form.cleaned_data['username']
        password= form.cleaned_data['password1']
        user = authenticate(username = username  , password = password)
        login(request,user)
        messages.success(request,"You have register sucess")
        return redirect('home')
      else:
        messages.success(request,"You have register falid")
        return redirect('register')
    else:
      return render(request,'register.html',{'form': form})
    

def product(request,pk):
  product = Perfume.objects.get(id=pk)
  return render(request,'product.html',{'product':product})