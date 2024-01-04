from django.db import models
from Signup.models import MyUser
from django.utils import timezone
from datetime import datetime
import pytz
from django.utils.timezone import is_aware, make_naive

# Create your models here.
class ProductDetails(models.Model):
    user_id       = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='products')
    product_id    = models.AutoField(primary_key=True)
    product_name  = models.CharField(max_length=255)
    product_desc  = models.CharField(max_length=500)
    min_bid_price = models.IntegerField()
    end_date      = models.DateTimeField()
    status        = models.BooleanField(default=True)
    product_img   = models.ImageField(upload_to='productImg/', max_length=255)
    
    def __str__(self):
        return self.product_desc
    
    def update_status(self):     
        # Get the current timezone
        current_tz = timezone.get_current_timezone()
        # Check if the end_date is aware or naive
        if is_aware(self.end_date):
            # Option 1: Remove the tzinfo and make it naive
            end_date = make_naive(self.end_date)
        else:
            # Keep it as it is
            end_date = self.end_date
            # Make the end_date aware of the current timezone
            end_date = current_tz.localize(end_date)
            # Compare with the current datetime
            if end_date < timezone.now():
                # Set the status to False
                self.status = False
                # Save the changes
                self.save()

class BidderPriceList(models.Model):
    bid_id     = models.AutoField(primary_key=True)
    user_id    = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    bidPrice   = models.IntegerField()

    def __str__(self):
        return f"{self.user_id} bid {self.bidPrice} on {self.product_id}"

                    