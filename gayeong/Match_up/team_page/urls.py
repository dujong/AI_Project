from django.contrib import admin
from django.urls import path, include 

from.import views

app_name = "team_page"

urlpatterns = [
    path('management/', views.management, name = 'management'),
    path('teaminfo/', views.teaminfo, name = "teaminfo"),
    path('testpage/', views.testpage, name = "testpage"),
]
