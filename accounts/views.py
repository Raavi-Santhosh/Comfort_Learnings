from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(request, username=form_data['username'],
                                password=['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled Account')
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})



