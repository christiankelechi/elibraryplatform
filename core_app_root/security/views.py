from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import requests
from rest_framework.response import Response
from .forms import *
from core_app_root.security import authenticate
from core_app_root.security.authenticate import FaceIdAuthBackend
from core_app_root.security.forms import AuthenticationForm
from core_app_root.security.utils import prepare_image
from elibraryplatform import settings
from . import base_url
from rest_framework import status
from .forms import UserCreationForm
app_name='security'
def login(request):
    context=""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            print("valid")
            face_image = prepare_image(form.cleaned_data['image'])
            print(face_image)
            face_id = FaceIdAuthBackend()
            email=request.POST['email']
            password=request.POST['password']
            signin_data={
                "email":email,
                "password":password,
                }
            
            main_url=base_url.main_url+"login/"
            user = face_id.authenticate(username=email, password=password, face_id=face_image)
            if user is not None:
                singin_response=requests.post(main_url,json=signin_data)

                if singin_response.status_code==200:
                    
                    singin_response=singin_response.json()
                    print(singin_response)
                    return redirect('dashboard_app:dashboard')
                    
                # username = form.cleaned_data['email']
                # password = form.cleaned_data['password']
                return redirect('dashboard_app:dashboard')
            else:
                form.add_error(None, "Username, password or face id didn't match.")
        else:
            print("not valid")
    else:
        print("not valid")
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'auth/login.html', context)


    


# Create your views here.
def signup(request):
    if request.method=='POST':
        # form = UserCreationForm(request.POST, request.FILES)
        
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
    form = UserCreationForm()
    context = {'form': form}
    
    return render(request,'auth/signup.html',context)

def face_recognition(request):
    return render(request,'auth/face-recognition.html')

def register(request):
    if  request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('security:login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'django_two_factor_face_auth/signup.html', context)


def face_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            face_image = prepare_image(form.cleaned_data['image'])

            face_id = FaceIdAuthBackend()
            user = face_id.authenticate(username=username, password=password, face_id=face_image)
            if user is not None:
                login(request, user)
                return redirect('security:login')
            else:
                form.add_error(None, "Username, password or face id didn't match.")
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'auth/face-recognition.html', context)