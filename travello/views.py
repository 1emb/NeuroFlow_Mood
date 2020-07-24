from django.shortcuts import render, redirect
from .models import userMood
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime
from datetime import timedelta


# Create your views here.
def index(request):
    return render(request, "index.html")


def mood(request):
    '''
    Render index.html with mood and streak information from query
    Update userMood database 
    
    request: HTTP request
    '''
    mood = request.GET['mood']
    username = request.GET['username']
    now = datetime.datetime.now()
    streak = 1 #user current login streak
    countDayBack = now - timedelta(days = streak)
    #counts user current login streak
    while (userMood.objects.filter(username=username).filter(date = countDayBack.date())): 
        streak += 1 
        countDayBack = now - timedelta(days = streak)
    
    if User.objects.filter(username=username).exists(): #check whether user existed
        user = userMood(username = username, mood = mood, streak = streak)
        user.save() #update userMood database
        return render(request, "index.html",{'mood':mood,'streak':user.streak})
    else:
        print("error user not found while inputing mood")
        return render(request, "index.html")
