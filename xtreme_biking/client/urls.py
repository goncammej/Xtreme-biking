from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.create_user, name='register'),
]