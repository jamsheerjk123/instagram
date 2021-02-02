from django.shortcuts import render,HttpResponse
from .forms import Login

def login(request):
   if request.method=='POST' :
      form=Login(request.POST)
      return HttpResponse('hai')

   form=Login()
   return render(request,'login.html',{'form':form})
   

