from django.urls import path
from . import views

urlpatterns = [
    path('admin_pannel/admin', views.AdminPannel, name='adminPannel'),
    path('<int:userID>/home/', views.Home, name='home'),
    path('<int:userID>/home/create/',views.CreateBidForm, name='createBid'),
    path('<int:userID>/home/auction_item/',views.AuctionItem.as_view(), name='auctionItem'),    
    path('<int:userID>/home/<int:productID>/', views.ProductDetail, name='productDetail'),       
    path('<int:userID>/home/my_posted_items/', views.MyPostedItems, name='myPostedItems')
]

