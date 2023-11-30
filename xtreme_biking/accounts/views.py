from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from .forms import SignUpForm


""" class UserView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user
 """

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})