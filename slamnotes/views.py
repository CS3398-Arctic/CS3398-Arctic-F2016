"""slamnotes Views Configuration

Several function-based views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/views/
"""

# import datetime

from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Note, NoteForm, SignupForm, LoginForm


def index(request):
    """Home page view"""
    account_created = False

    if request.method == 'POST':
        form_login = LoginForm(request.POST, request.FILES)
        form_signup = SignupForm(request.POST, request.FILES)

        if "login-form" in request.POST and form_login.is_valid():
            User.objects.login(**form_login.cleaned_data)
        elif "signup-form" in request.POST and form_signup.is_valid():
            User.objects.create_user(**form_signup.cleaned_data)
            account_created = True
    else:
        form_login = LoginForm()
        form_signup = SignupForm()

    return render(request, 'index.html',
                  {
                      'form_login': form_login,
                      'form_signup': form_signup,
                      'account_created': account_created,
                  })


def channel(request):
    """Channel view"""
    all_notes = Note.objects.order_by('-id')

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if request.user.is_authenticated() and form.is_valid():
            form.save()
    else:
        form = NoteForm()

    return render(request, 'channel.html',
                  {
                      'form': form,
                      'notes': all_notes,
                      'user': request.user,
                  })
