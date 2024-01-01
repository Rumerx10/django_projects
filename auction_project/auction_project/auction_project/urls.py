from django.contrib import admin
from django.urls import path,include
from Signup import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myusers/',views.Myuser),
    path('',include('Signup.urls')),
]
