from django.contrib import admin
from django.urls import path,include
from Signup import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myusers/',views.Myuser),
    path('',include('Signup.urls')),
    path('',include('Home.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    