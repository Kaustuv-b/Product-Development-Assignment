from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .form import CreateUserForm, UserForm
from .models import Video, Comment 


# login
def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None: 
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'Incorrect Username or Password')

    context =  {'page': page}
    return render(request, 'main/login_register.html', context)

# logout
def logoutuser(request):
    logout(request)
    return redirect('home')

def registerUser(request):

    page = 'register'

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save() 
            login (request, user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong, Please try again')

    context = {'page': page, 'form': form}
    return render (request, 'main/login_register.html', context)

# homepage
def home(request):
    return render(request, 'main/home.html')



# videolist page
def videoList(request):

    video = Video.objects.all()

    context = {'video':video}
    return render(request, 'main/recorded_videos.html', context)


# watchvideo page
# @login_required(login_url = '/login')
def watchVideo(request, pk):
    videos = Video.objects.get(id = pk)
    comments = videos.comment_set.all()

    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            video = videos,
            body = request.POST.get('body'),
        )
        return redirect('watch-video', pk = videos.id)

    context = {'video': videos, 'comments':comments}
    return render(request, 'main/watch_videos.html', context)


@login_required(login_url = 'login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id = pk)

    if not request.user.is_superuser:
        return redirect ('watch-video', pk = comment.video.id)

    if request.method == 'POST':
        comment.delete()
        return redirect ('watch-video', pk = comment.video.id)
    
    context = {'obj': comment}
    return render (request, 'main/delete-comment.html', context)

@login_required(login_url = 'login')
def userProfile(request):
    return render (request, 'main/profile.html')


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = user)
        if form.is_valid:
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'main/update_user.html', context)


def passwordReset(request):


    context = {}
    return render(request, 'main/password-reset.html', context)

def live(request):
    return render(request, 'main/live.html')

def schedule(request):
    return render(request, 'main/schedule.html')

def about(request):
    return render(request, 'main/about.html')

def medal(request):
    return render(request, 'main/medal.html')

