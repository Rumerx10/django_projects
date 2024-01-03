from django.shortcuts import render,redirect
from Signup.models import MyUser
from .models import ProductDetails
from datetime import datetime
from django.urls import reverse

# Create your views here.
def Home(request,userID):
    products = ProductDetails.objects.all()
    for product in products:
        product.update_status()
        # Filter the products by status
        products = products.filter(status=True)
    return render(request, 'home.html', {'products': products})

def CreateBidForm(request,userID):
    if request.method=="POST":
        user_id = MyUser.objects.get(user_id=userID)
        product_name = request.POST.get('productName')
        product_desc = request.POST.get('productDesc')
        min_bid_price = request.POST.get('minimunBidPrice')
        product_img = request.FILES.get('productImg')
        end_date = request.POST.get('endDate')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        print(user_id,product_name,product_img)        
        newProduct = ProductDetails(user_id=user_id,product_name=product_name,product_desc=product_desc,min_bid_price=min_bid_price,product_img=product_img,end_date=end_date)
        newProduct.update_status()      
        newProduct.save()
        
        url = reverse('home', kwargs={'userID': userID})
        return redirect(url)
    return render(request,'createBid.html',{'userID':userID})

def MyPostedItems(request,userID):
    myItems = ProductDetails.objects.filter(user_id_id=userID)
    return render(request,'myPostedItems.html',{'myItems':myItems})