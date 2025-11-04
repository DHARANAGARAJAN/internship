from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import RegisteredUser

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
# Assuming these models are in the same app

def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')

def browserpage(request):
    return render(request, 'browsercourse.html')  # For testing

def quizpro(request):
    return render(request, 'quizpro.html')    

def about(request):
    return render(request,'about.html')




def fullstack(request):
    return render(request, 'viewcourse/fullstack.html')


def datascience(request):
    return render(request, 'viewcourse/data.html')


def reactjs(request):
    return render(request, 'viewcourse/react.html')  

def java(request):
    return render(request, 'viewcourse/java.html')


def cloud(request):
    return render(request, 'viewcourse/cloud.html')



def cprogramming(request):
    return render(request, 'viewcourse/cc.html')


def cybersecurity(request):
    return render(request, 'viewcourse/cyber.html')

def excel(request):
    return render(request, 'viewcourse/ex.html')         




# Register Page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        course = request.POST['course']
        RegisteredUser.objects.create(username=username, password=password, course=course)
        return redirect('login')
    return render(request, 'register.html')

# Login Page


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"login attempt by:{username}")

        try:
            user = RegisteredUser.objects.get(username=username, password=password)
            request.session['username'] = user.username  # optional: to keep session
            request.session['course'] = user.course
            return redirect('dashboard')  # Make sure you have this URL name in urls.py
        except RegisteredUser.DoesNotExist:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')      

def dashboard(request):
    username = request.session.get('username')
    course = request.session.get('course')
    return render(request, 'dashboard.html', {'username': username, 'course': course})    

def c1_page(request):
    username = request.session.get('username')
    course = request.session.get('course')
    return render(request, 'viewcourse/c1.html', {'username': username, 'course': course})

def c2_page(request):
    return render(request, 'viewcourse/c2.html')

def j1_page(request):
    username = request.session.get('username')
    course = request.session.get('course')
    return render(request, 'viewcourse/j1.html', {'username': username, 'course': course})
                   
def r1_page(request):
    username = request.session.get('username')
    course = request.session.get('course')
    return render(request, 'viewcourse/r1.html', {'username': username, 'course': course})

