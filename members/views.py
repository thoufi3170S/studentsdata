from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    return render(request,'login.html')
def frst(request):
    return render(request,'nav.html')
def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username  = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    
    if password1 == password2:
      user = User.objects.create_user(username=username , password=password1 , email=email , first_name=first_name , last_name=last_name)
      user.save()
      print('user created')
      return render(request,'login.html')
      
    else:
      print("password is'nt match...")
      return render(request,'register.html')
  
      

  else:
    return render(request,'register.html')




