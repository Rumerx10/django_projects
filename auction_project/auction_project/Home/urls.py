from django.urls import path
from . import views

urlpatterns = [
    path('<int:userID>/home/', views.Home, name='home'),       
    path('<int:userID>/home/create/',views.CreateBidForm, name='createBid'),
    path('<int:userID>/home/my_posted_items/', views.MyPostedItems, name='myPostedItems')
]

