from django.shortcuts import render,redirect,get_object_or_404
from Signup.models import MyUser
from .models import ProductDetails,BidderPriceList
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



def ProductDetail(request, userID, productID):
    item = get_object_or_404(ProductDetails, product_id=productID)
    context= {'item':item, 'userID':userID}
    if request.method=="POST" and item.user_id_id != userID:    
        user = get_object_or_404(MyUser, user_id=userID)   
        product = get_object_or_404(ProductDetails, product_id=productID)
        bidPrice = request.POST.get('bidPrice')            
        # print(user,product,bidPrice)

        # update or create a newBid object with the user and product
        newBid, created = BidderPriceList.objects.update_or_create(user_id=user, product_id=product, defaults={'bidPrice': bidPrice})
        # no need to save the newBid object as update_or_create does it automatically

        bidList = BidderPriceList.objects.filter(product_id=productID)
        context = {'item':item,'userID':userID,'bidList':bidList}
        return render(request, 'productDetail.html', context)

    return render(request, 'productDetail.html', context)




