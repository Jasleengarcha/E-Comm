from django.shortcuts import render,  HttpResponse, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if(request.method == 'POST'):
        mail_id = request.POST.get('mail_id')
        psw = request.POST.get('psw')

        user = authenticate(username= mail_id, password= psw)
        if user:
            login(request, user)
            qs = SignUp.objects.filter(email=mail_id)
            info = {'query_set': qs}
            if qs:
                return render(request, 'index.html', context=info)
            return render(request, 'index.html')
        else:
            return render(request, 'signin.html')

    return render(request, 'signin.html')

def signup(request):
    if(request.method == 'POST'):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email_id = request.POST.get('email_id')
        phn = request.POST.get('phn')
        adrs = request.POST.get('adrs')
        pswd = request.POST.get('pswd')

        user = User.objects.create_user(username= email_id, password= pswd, first_name=fname)
        user.save()

        signup = SignUp(
            first_name = fname,
            last_name = lname,
            email = email_id,
            phone = phn,
            address = adrs
        )
        signup.save()
        
    return render(request, 'signup.html')

def user_details(request):
    user_detail = []
    user = SignUp.objects.all()
    for i in user:
        user_dict = {}
        user_dict["Fname"] = i.first_name
        user_dict["Email"] = i.email 
        user_dict["PhoneNumber"] = i.phone
        user_detail.append(user_dict) 

    return JsonResponse(user_detail, safe=False)

def healthy_food(request):
    return render(request, 'healthy-food.html')

def logout_view(request):
    logout(request)
    return redirect(signin)