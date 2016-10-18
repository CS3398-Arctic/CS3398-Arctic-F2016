"""slamnotes Views Configuration

Several function-based views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/views/
"""
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render
from .models import Note, NoteForm
import datetime


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


# def view_text_body(request):
#     return TemplateResponse(request, 'notes/index.html', {})


def view_note_id(request, note_id):
    return HttpResponse("Note ID: %s." % note_id)


def note_test(request):
    """Note test page view"""
    # most_recent_note = Note.objects.latest('id')
    all_notes = Note.objects.order_by('-id')
    # body_text = most_recent_note.body_text

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            now = datetime.datetime.now()
            html = "<html><body>Current Time: %s.</body></html>" % now
            return HttpResponse(html)
            # form.save()
            # body_text = form.cleaned_data['body_text']
    else:
        form = NoteForm()

    return render(request, 'note_test.html',
                  {
                      'form': form,
                      # 'body_text': body_text,
                      'notes': all_notes,
                  })
