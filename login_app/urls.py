# accounts/urls.py
from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify/<uidb64>/<token>/', views.verify_email, name='verify'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
