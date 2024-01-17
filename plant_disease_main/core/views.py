from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from .forms import LoginForm, RegisterForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from .decorators import *


#Home-Page
def index(request):
  return render(request, 'home/index.html')


#Login-Page
def login(request):
   if request.method =="POST":
      print("hello")
      username=request.POST.get("username")
      password=request.POST.get("password")
      user=auth.authenticate(username=username,password=password)
      print(username,password)
      print(user)
   
      if user is not None:
          print('hii')
          auth.login(request,user)
          return redirect('/')
      else:
          return redirect('login')
   return render(request, 'credential/login.html')
   

#Register-Page
def register(request):
   if request.method == "POST":
     username=request.POST.get("username")
     email = request.POST.get("email")
     password=request.POST.get("password")
     for name in User.objects.all():
        if name.username == username:
            messages.warning(request,"Username already exits")
            return redirect('register')

     User.objects.create_user(username = username, email= email, password = password)
     return redirect('login')
   return render(request, 'credential/signup.html')


#Logout-Page
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url='login')
def user_page1(request):
   plants = Plant.objects.all()
   return render(request, 'profiles/plant_library.html', {'plants': plants,})

@login_required(login_url='login')
@allowed_user(allowed_roles=['manager', 'admin'])
def manager(request):
   plant = Plant.objects.all()
   if request.method == "POST":
      name = request.POST.get('name')
      scientific_name = request.POST.get('scientific_name')
      description = request.POST.get('description')
      image = request.FILES['image']
      Mostly_caused_disease_name = request.POST.get('Mostly_caused_disease_name')
      solution = request.POST.get('solution')
      disease_image = request.FILES['disease_image']
      Plant.objects.create(name = name, scientific_name = scientific_name, description = description, image = image, Mostly_caused_disease_name = Mostly_caused_disease_name, solution = solution, disease_image = disease_image)
      return redirect('/')
   return render(request, 'manager/manager.html')

@login_required(login_url='login')
def plant_description(request, plant_id):
   plant = Plant.objects.get(id = plant_id)
   return render(request, 'profiles/plant_description.html', {'plant':plant,})

@login_required(login_url='login')
def user_problem(request):
   body = request.user
   userplants = UserPlant.objects.all()
   return render(request, 'profiles/problem.html', {'userplants':userplants, 'body':body,})

@login_required(login_url='login')
def add_problem(request):
   if request.method == "POST":
      name = request.POST.get('name')
      image = request.FILES['image']
      description = request.POST.get('description')
      UserPlant.objects.create(name = name, image = image, description = description, created_by = request.user, created_at = datetime.now())
      return redirect('user_problem')
   return render(request, 'profiles/add_problem.html')

@login_required(login_url='login')
def add_comment(request, plant_id):
    userplant = get_object_or_404(UserPlant, id=plant_id)
    if request.method == "POST":
        suggestion_text = request.POST.get('suggestion')
        try:
            suggestion = UserSuggestion.objects.create(
                suggestion=suggestion_text,
                plant=userplant,
                given_by=request.user,
                created_at=datetime.now()
            )
            return redirect('user_problem') 
        except Exception as e:
            print(f"Error creating UserSuggestion: {e}")
    return render(request, 'profiles/add_comment.html', {'userplant': userplant})

@login_required(login_url='login')
def read_comment(request, plant_id):
    userplant = get_object_or_404(UserPlant, id = plant_id)
    usersuggestion = UserSuggestion.objects.all()

    return render(request, 'profiles/read_comment.html', {'userplant':userplant, 'usersuggestion':usersuggestion,})

@login_required(login_url='login')
def delete_comment(request, comment_id):
    comment = UserPlant.objects.get(id = comment_id)
    comment.delete()
    return redirect('user_problem')

@login_required(login_url='login')
def daily_updates(request):
   updates = DailyUpdates.objects.all()
   return render(request, 'profiles/daily_updates.html', {'updates':updates,})

@login_required(login_url='login')
@allowed_user(allowed_roles=['manager', 'admin'])
def updates(request):
   if request.method == "POST":
      name = request.POST.get('name')
      image = request.FILES['image']
      description = request.POST.get('description')
      DailyUpdates.objects.create(name = name, image = image, description = description, created_at = datetime.now(), created_by = request.user)
      return redirect('/')
   return render(request, 'profiles/updates.html')
