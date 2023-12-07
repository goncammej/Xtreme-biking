from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    # path('profile/',  login_required(UserView.as_view()), name='profile'),
    path('signup/', signup, name='signup')
]
