"""slamnotes Views Configuration

Several function-based views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/views/
"""
import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Note, NoteForm


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


def note_test(request):
    """Note test page view"""
    all_notes = Note.objects.order_by('-id')

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if request.user.is_authenticated() and form.is_valid():
            form.save()
    else:
        form = NoteForm()

    return render(request, 'note_test.html',
                  {
                      'form': form,
                      'notes': all_notes,
                      'user': request.user,
                  })


def user_test(request):
    """user test page view"""
    return render(request, 'registration/login.html')
