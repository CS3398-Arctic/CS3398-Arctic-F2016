
import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .models import Note, NoteForm, UserForm, LoginForm


def index(request):
    """Home page view"""
    return render(request, 'index.html')


def view_time(request):
    now = datetime.datetime.now()
    html = "<html><body>Current Time: %s.</body></html>" % now
    return HttpResponse(html)


def text_body_view(request):
    most_recent_note = Note.object.order_by('-created_date')[:5]
    output = ', '.join([n.body_text for n in most_recent_note])
    return HttpResponse(output)


def view_note_id(request, note_id):
    return HttpResponse("Note ID: %s." % note_id)


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


def user_test(request):
    """user test page view"""
    return render(request, 'login.html')


def create_account(request):
    """account creation page"""
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return render(request, 'account_created.html')
    else:
        form = UserForm()
    return render(request, 'create_account.html',
                  {
                      'form': form,
                  })


def login(request):
    """login page"""
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            User.objects.login(**form.cleaned_data)
            return render(request, 'login_successful.html')
    else:
        form = LoginForm()
    return render(request, 'login.html',
                  {
                      'form': form,
                  })


def account_created(request):
    """account created test page"""
    return render(request, 'account_created.html')