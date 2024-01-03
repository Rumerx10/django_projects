from django.contrib import admin
from .models import ProductDetails
# Register your models here.

class ProductDetailsAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','product_desc','min_bid_price','product_img','end_date','status','user_id')

admin.site.register(ProductDetails,ProductDetailsAdmin)