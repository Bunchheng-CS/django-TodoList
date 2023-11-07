from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import TodoTask
from django.contrib.auth.models import User
from .forms import TodoTaskForm, UserRegisterFrom
# Create your views here.


def register_page(request):
    form = UserRegisterFrom()
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base:home_page')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'form': form}
    return render(request, 'base/register_and_login_form.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('base:home_page')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
          # check have user or not
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')
        # check username nad password
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base:home_page')
        else:
            messages.error(request, 'Username OR password does not exit')

        

    return render(request, 'base/register_and_login_form.html',{'page':'login'})


def logout_page(request):
    logout(request)
    return redirect('base:home_page')


def home_page(request):
    tasks = {}
    if request.user.is_authenticated:
        tasks = TodoTask.objects.all().filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'base/home.html', context)


def create_task(request):
    form = TodoTaskForm()
    if request.method == 'POST':
        if request.POST.get('complete') == 'on':
            isComplete = True
        else:
            isComplete = False
        TodoTask.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            complete=isComplete,
        )
        return redirect('base:home_page')
    print(request.path)
    context = {'form': form}
    return render(request, 'base/create_update_task.html', context)


def update_task(request, pk):
    task = TodoTask.objects.get(id=pk)
    form = TodoTaskForm(instance=task)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        if request.POST.get('complete') == 'on':
            task.complete = True
        task.save()
        return redirect('base:home_page')
    context = {'form': form, 'task': task}
    return render(request, 'base/create_update_task.html', context)


def delete_task(request, pk):
    task = TodoTask.objects.get(id=pk)
    if task.complete == True:
        task.delete()
        return redirect('base:home_page')
    elif request.method == 'POST':
        task.delete()
        return redirect('base:home_page')
    return render(request, 'base/delete_task.html', {'obj': task.title})
