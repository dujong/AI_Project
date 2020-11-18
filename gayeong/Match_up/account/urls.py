from django.contrib import admin
from django.urls import path, include 

from.import views

app_name = "account"

urlpatterns = [
    path('', views.main, name = 'main'),
    path('log_in/', views.log_in, name = "log_in"),
    path('log_out/', views.log_out, name = "log_out"),
    path('sign_up/', views.sign_up, name = "sign_up"),
    path('my_page/', views.my_page, name = "my_page"),
]
