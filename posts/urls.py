# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    path(route='',view=views.PostsFeedView.as_view(),name='feed'),
    path(route='posts/<int:pk>/', view=views.PostView.as_view(), name='one_post'),
    path(route='posts/new/',view=views.CreatePostView.as_view(),name='create'),
]