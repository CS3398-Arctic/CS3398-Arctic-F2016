"""slamnotes Views Configuration

Several function-based views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/views/
"""
from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return render(request, 'index.html')
