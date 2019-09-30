from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from users.forms import RegistrationForm
from users.models import Users


def login_view(request):
    if request.method == 'GET':
        return render(request, "main_login_form.html", context={
            "error": False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            try:
                user = Users.objects.get(username=username)
                user.incorrect_attempts += 1
                if user.incorrect_attempts > settings.INCORRECT_ATTEMPTS_LIMIT:
                    user.is_active = False
                user.save()
            except Users.DoesNotExist:
                pass
            return render(request, "main_login_form.html.html", context={
                "error": True
            })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.verify_email()
            return render(request, "main.html")
    else:
        form = RegistrationForm()
    return render(request, "register_form.html", context={
        "form": form
    })