from django.contrib import admin
from Signup.models import MyUser
# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('user_id','email','password')
admin.site.register(MyUser,MyUserAdmin)