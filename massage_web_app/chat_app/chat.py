from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='home')
def chat(request):
    return render(request, 'chat_app/index.html')
