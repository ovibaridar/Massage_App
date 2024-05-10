from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request, 'chat_app/signin.html')


def signup(request):
    return render(request, 'chat_app/register.html')


def creat_acount(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        gmail = request.POST.get('email')
        password = request.POST.get('password')
        con_p = request.POST.get('confirm_password')

        # You may want to add validation and error handling here
        if User.objects.filter(email=gmail).exists():
            error = "This email is already in use."
            return render(request, 'chat_app/register.html', {'error': error})
        # Save the data to the database using the renamed model
        else:
            my_user = User.objects.create_user(name, gmail, password)
            my_user.save()
            return redirect('home')

    return render(request, 'vote_application/Sign_up_.html')
