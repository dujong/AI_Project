from django.contrib import admin
from django.urls import path, include 

from.import views

app_name = "community"

urlpatterns = [
    path('free_board/', views.free_board, name = 'free_board'),
    path('review_board/', views.review_board, name = "review_board"),
    path('hire_board/', views.hire_board, name = "hire_board"),
    path('createPost_free/', views.createPost_free, name = "createPost_free"),
    path('createPost_review/', views.createPost_review, name = "createPost_review"),
    path('createPost_hire/', views.createPost_hire, name = "createPost_hire"),
    path('postDetail/<int:id>/', views.postDetail, name = "postDetail"),
]
