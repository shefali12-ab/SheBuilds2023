from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or Password Incorrect')
    return render(request, 'authenticate/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created')
                return redirect('login')
        else:
            form = CreateUserForm()
        context = {
            'form': form
        }
    return render(request, 'authenticate/register.html', context)

def homepage(request):
    return render(request, 'home.html')


def logout_page(request):
    logout(request)
    return redirect('login')

def quiz(request):
    if request.method == 'POST':
        questions = QuesModel.objects.all()
        score = 0
        for q in questions:
            if "option1" == request.POST.get(q.question):
                score += 2
            elif "option2" == request.POST.get(q.question):
                score += 1
            else:
                score += 0
        result = ""
        if score > 25:
            result = "You might have a severe case of Postpartum depression. We strongly recommend you to get an official diagnosis as soon as possible."
        elif score > 10:
            result = "You might have Postpartum depression. We recommend you to get an official diagnosis."
        else:
            result = "You might not have Postpartum depression. However, if you feel like we made a mistake we recommend you to get an official diagnosis."

        context = {
            'result': result
        }
        return render(request,'quiz/results.html', context)
    else:
        questions = QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz/quiz.html', context)

def discussion(request):
    discussion = DiscussionModel.objects.all()
    context = {
        'discussion': discussion
    }
    return render(request, 'discussions/discussion.html', context)

def add_discussion(request):
    if request.method == 'POST':
        form = AddDiscussion(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('discussion')
    else:
        form = AddDiscussion()
        context = {
            'form': form
        }
    return render(request, 'discussions/add_discussion.html', context)

def view_discussion(request, pk):
    discussion = DiscussionModel.objects.get(id=pk)
    comments = CommentModel.objects.filter(discussion=discussion)
    form = AddComment()
    context = {
        'discussion': discussion,
        'form' : form,
        'comments' : comments
    }
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.discussion = discussion
            instance.save()
            form = AddComment()
    else:
        form = AddComment()
    return render(request, 'discussions/view_discussion.html', context)