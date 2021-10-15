"""Users URLs"""

# Django
from django.urls import path

#View
from . import views

urlpatterns = [

    #management
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('me/profile/', views.UpdateProfileView.as_view(), name='update'),

    #posts
    path('<str:username>/', views.UserDetailView.as_view(), name='detail'),
    # path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
] 

