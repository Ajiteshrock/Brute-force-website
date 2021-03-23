from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def donator(request):
    return render(request,'login.html')

def register(request):

    if request.method=="POST":
        user=request.POST['username']
        emai=request.POST['email']
        passwor1=request.POST['password1']
        passwor2=request.POST['password2']
        de=request.POST['des']
        nu=request.POST['num']
        if(passwor1==passwor2):
            if(models.organization.objects.filter(username=user)):
                messages.info(request,'Username Taken')
                return redirect('register')

            elif(models.organization.objects.filter(email=emai)):
                messages.info(request,'Email Taken')
                return redirect('donator')
            elif(models.organization.objects.filter(number=nu)):
                messages.info(request,'Number already taken')  
                return redirect('donator')        
            else:
                ins=models.organization(username=user,email=emai,password=passwor1,number=nu,des=de)
                ins.save()
                return redirect('donator')
        else:
            messages.info(request,'Password already taken')
            return redirect('donator')        
    else:   
        return render(request,'register.html')  
      