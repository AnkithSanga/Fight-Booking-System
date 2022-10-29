from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from FlightBooking.models import User      
from django.urls import reverse
from django.contrib.auth import authenticate,login as auth_login

# Function for registration page.
def register(request):
    registered=False
    if request.method=="POST":
        user_id=request.POST.get('UserId')            #userid,Username,email,Password,gender need to match with the register page ids
        username=request.POST.get('Username') 
        email=request.POST.get('email')
        password=request.POST.get('PassWord')
        check_user = Users.objects.filter(email=email).first()      #checking if the user is already has an account or not
        if check_user :
            return HttpResponse("user alread has an account please login!")
        else:
            profile=User(user_id=user_id,username=username,email=email,password=password)       #saving the details into model or database created 
            profile.save() 
            registered=True
            return HttpResponse("User successfully registered")
    return render(request,'register.html') 

def login(request):
    if request.method == "POST":
        userN=request.POST.get('Username')
        passW=request.POST.get('PassWord')
        user = authenticate(username=userN,password=passW)       #Authenticating username and password of a user
        if user:
               auth_login(request,user)
               return HttpResponseRedirect(reverse('home'))     #if the user is authenticated then redirect the uder to home page

        else:
            print("username {} password {} not found".format(userN,passW))   #if user credentials or not correct 
            return HttpResponse("invalid crendentials")
    else:
        return render(request,'login.html')
def home(request):
    return render(request,'home.html')

def booking(request):
    return render(request,'booking.html')
