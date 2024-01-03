from django.shortcuts import render,redirect,get_object_or_404
from Signup.models import MyUser

# Create your views here.

def Signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email,password)
        olduser = MyUser.objects.filter(email__exact=email)        
        if olduser.exists():
            user = get_object_or_404(MyUser, email=email)
            user_id = user.user_id
            print(user_id)
            # return render(request,'home.html',{'userID':user_id})
            return redirect(f'{user.user_id}/home', user_id=user.user_id)
        else:
            newUser = MyUser(email=email,password=password)
            newUser.save()
            user = get_object_or_404(MyUser, email=email)
            user_id = user.user_id
            print(user_id)
            # return render(request,'home.html',{'userID':user_id})
            return redirect(f'{user.user_id}/home', user_id=user.user_id)
        
    return render(request,'index.html')

def Myuser(request):
    myuser = MyUser.objects.all()
    return render(request, 'myuser.html',{'users':myuser})

