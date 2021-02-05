from django.shortcuts import render,HttpResponse,redirect
from .forms import SignUp
from django.contrib.auth import authenticate, login,logout
from posts import views

def login_view(request):
   if request.method=='POST':
      email=request.POST['email']
      password=request.POST['password']
      user=authenticate(email=email,password=password)
      if user:
         return redirect('posts:home')
      else:
         return render(request,'accounts/login.html',{'error':True,'error_msg':"invalid email or password"})
   else:
      return render (request,'accounts/login.html')
   
def sign_up(request):
   if request.method=="POST":

      form=SignUp(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/accounts/login')
      return render(request,'accounts/signup.html',{'form':form})



   else:
      form=SignUp()
      return render(request,'accounts/signup.html',{'form':form})


def signout(request):
   logout(request,user)
   return redirect('accounts:login')
