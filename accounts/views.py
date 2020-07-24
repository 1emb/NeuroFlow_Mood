from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    '''
    Let user sign up
    Update User database 
    
    request: HTTP request
    '''    
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists(): #check if username has been taken or not
            messages.info(request,"username taken")
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, password = password,email = email, first_name=first_name, last_name = last_name)
            user.save() #update User database
            print("usercreated", username, email)
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    '''
    Let user log in
    
    request: HTTP request
    '''      
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password) #check if username and password match
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credential")
            return redirect('login')
    else:
        return render(request, 'login.html')

def home(request):
    '''
    Render home page
    '''      
    return redirect('/')

def logout(request):
    '''
    Let user log out
    Render home page
    '''      
    auth.logout(request)
    return redirect('/')

