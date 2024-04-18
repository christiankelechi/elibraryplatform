from django.urls import path
from . import views

app_name='core_app_root'
urlpatterns=[
    path('',views.index,name='index')
]