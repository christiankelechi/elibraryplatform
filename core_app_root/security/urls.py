from django.urls import path
from .views import signup,login
app_name='security'
urlpatterns = [
    path("auth/signup/",signup,name='signup'),
    path('auth/login/',login,name='login')
]
