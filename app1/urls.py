from django.urls import path,include
from app1.views import *

app_name = 'app1'
urlpatterns = [
    path('register/',register,name='register'),
]