from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signUp/', views.signUp, name='signUp'),
   path('login/',views.user_login,name='login'),
   path('dashboard/',views.dashboard,name='dashboard'),
]
