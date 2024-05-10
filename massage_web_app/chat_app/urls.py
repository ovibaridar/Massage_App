from django.urls import path

from . import chat
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign up', views.signup, name='sign up'),
    path('creat_acount', views.creat_acount, name='creat_acount'),
    path('chat', chat.chat, name='chat'),
    path('login', views.log_in_, name='login')

]
