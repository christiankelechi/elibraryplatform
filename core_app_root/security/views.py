from django.shortcuts import render,redirect
import requests
from rest_framework.response import Response
from . import base_url
from rest_framework import status
app_name='security'
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        signin_data={
            "email":email,
            "password":password,
            }
        main_url=base_url.main_url+"login/"
        singup_response=requests.post(main_url,json=signin_data)

        if singup_response.status_code==200:
            singup_response=singup_response.json()
            print(singup_response)
            # context="Signup Successful"
            # return render(g)
        
            
        
            return redirect('core_app_root:index')
        else:
            # full_url=f"{base_url}auth/login"
            return redirect("security:login")
    
    return render(request,'auth/login.html')


# Create your views here.
def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if str(password)==str(confirm_password):
            signup_data={
            "email":email,
            "username":username,
            "password":password,
            "confirm_password":confirm_password
            }
            main_url=base_url.main_url+"register/"
            singup_response=requests.post(main_url,json=signup_data)

            if singup_response.status_code==201:
                singup_response=singup_response.json()
                print(singup_response)
                # context="Signup Successful"
                # return render(g)
            
            
            
                return redirect('security:login')
            else:
                # full_url=f"{base_url}auth/login"
                return redirect("security:signup")
        
    
    return render(request,'auth/signup.html')




