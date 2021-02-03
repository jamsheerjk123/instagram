from django.shortcuts import render,HttpResponse,redirect
from .forms import SignUp

def login_view(request):
   
   return render(request,'accounts/login.html')
   
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