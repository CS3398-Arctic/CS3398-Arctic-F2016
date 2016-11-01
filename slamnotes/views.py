"""slamnotes Views Configuration

Several function-based views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/views/
"""

# import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .models import Note, NoteForm, SignupForm, LoginForm, User


def index(request):
    """Home page view"""
    account_created = False
    invalid_login = False

    if request.method == 'POST':
        form_login = LoginForm(request.POST) if "login-form" in request.POST else LoginForm()
        form_signup = SignupForm(request.POST) if "signup-form" in request.POST else SignupForm()

        if "login-form" in request.POST:
            # Log user in
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
            else:
                # Return an 'invalid login' error message.
                invalid_login = True

        elif "signup-form" in request.POST and form_signup.is_valid():
            # Create new account
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
                      'invalid_login': invalid_login,
                  })


def channel(request):
    """Channel view"""
    all_notes = Note.objects.order_by('-id')

    if request.method == 'POST':
        posted_form = NoteForm(request.POST, request.FILES)
        if request.user.is_authenticated() and posted_form.is_valid():
            body_text = posted_form.cleaned_data['body_text']
            Note.objects.create(body_text=body_text, author=request.user)
    
    form = NoteForm()

    return render(request, 'channel.html',
                  {
                      'form': form,
                      'notes': all_notes,
                      'user': request.user,
                  })
