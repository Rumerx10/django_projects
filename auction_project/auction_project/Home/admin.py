from django.contrib import admin
from .models import ProductDetails,BidderPriceList
# Register your models here.

class ProductDetailsAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','product_desc','min_bid_price','product_img','end_date','status','user_id')

class BidderPriceListAdmin(admin.ModelAdmin):
    list_display=('bid_id','bidPrice','product_id', 'user_id')



admin.site.register(ProductDetails,ProductDetailsAdmin)
admin.site.register(BidderPriceList,BidderPriceListAdmin)