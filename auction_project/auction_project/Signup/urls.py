from django.urls import path
from . import views
urlpatterns = [
    path('', views.Signup, name='signup'),
    path('home/', views.Home, name='home'),    
]