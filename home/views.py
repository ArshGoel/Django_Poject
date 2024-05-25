from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login,get_user_model
from django.contrib import messages
from datetime import datetime
from home.models import createUser

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/create")
    return render(request,"index.html")

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username ,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect("/adminpage")
            else:
                login(request,user)
                return redirect("/userpage")
        else:
            return redirect("/create")
    return render(request,"login.html")
# def loginUser(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username ,password=password)
#         if User.objects.filter(username=username).exists():
#             if user.is_superuser:
#                 login(request,user)
#                 return redirect("/adminpage")
#             else:
#                 login(request,user)
#                 return redirect("/userpage")
#         else:
#             return redirect("/create")
#     return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")
 
def create(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists(): #To get the registered users in database
            messages.success(request,"User name already exists")
            return redirect('/login')
        else:
            contact = createUser(name=name,email=email,phone=phone,date=datetime.today(),username=username,password=password)
            contact.save()
            user = User.objects.create_user(username=username,password=password)
            messages.success(request,"Registration Successfull.. Please Login")
    return render(request, "create.html")

def adminpage(request):
    return render(request,"adminpage.html")
 
def userpage(request):
    return render(request,"userpage.html")