from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Signup.models import MyUser

# Create your views here.


def Signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
               
        olduser = MyUser.objects.filter(email__exact=email)        
        if olduser.exists():
            return redirect('home')
        else:
            newUser = MyUser(email=email,password=password)
            newUser.save()
            return redirect('home')
        
    return render(request,'index.html')

def Home(request):
    return render(request, 'home.html')









def Myuser(request):
    myuser = MyUser.objects.all()
    return render(request, 'myuser.html',{'users':myuser})





# def Signup(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         myuser = authenticate(email=email,password=password)
#         if myuser is not None:
#             login(request, myuser)
#             return redirect('home')
#         elif MyUser.objects.filter(email=email).exists():
#             messages.error(request, 'Invalid password.')
#             return redirect('signup')
#         elif not MyUser.objects.filter(email=email).exists():
#             newUser = MyUser(email=email,password=password)
#             newUser.save()
#             messages.success(request,'You have signedup successfully!')
#             return redirect('home')
#     return render(request,'index.html')