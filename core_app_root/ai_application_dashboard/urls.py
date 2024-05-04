from django.urls import path
from core_app_root.ai_application_dashboard import views

app_name="dashboard_app"
urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/search/',views.search,name='search'),
    path('dashboard/books/',views.book,name='books'),
    path('dashboard/books/recommendation/',views.recommendation,name='recommendation'),
    path('dashboard/books/save/',views.save_page,name='save'),
    path('dashboard/books/summarize/',views.summarize,name='summarize'),
    path('dashboard/citation/',views.reference_generator,name='citation')
   
    
]
