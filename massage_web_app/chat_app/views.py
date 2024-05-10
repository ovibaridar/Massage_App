from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect("chat")
    else:
        return render(request, 'chat_app/signin.html')


def log_in_(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve the user based on the email address
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None and check_password(password, user.password):
            # Password is correct, log in the user
            login(request, user)
            return redirect('chat')
        else:
            # Incorrect email or password
            error = 'Invalid email or password. Please try again.'
            return render(request, 'chat_app/signin.html', {'error': error})

    return render(request, 'chat_app/signin.html')


def signup(request):
    return render(request, 'chat_app/register.html')


def creat_acount(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        gmail = request.POST.get('email')
        password = request.POST.get('password')
        con_p = request.POST.get('confirm_password')

        if User.objects.filter(username=name).exists():
            error = "This username is already in use."
            return render(request, 'chat_app/register.html', {'error': error})

        if User.objects.filter(email=gmail).exists():
            error = "This email is already in use."
            return render(request, 'chat_app/register.html', {'error': error})

        # Save the data to the database using the renamed model
        my_user = User.objects.create_user(name, gmail, password)
        my_user.save()
        return redirect('home')

    return render(request, 'chat_app/register.html')
