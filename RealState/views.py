import random
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'list.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

def events(request):
    event = {
        'title': 'Conference',
        'description': 'Join us for an insightful conference on the latest industry trends.',
        'image': 'https://example.com/conference.jpg'
    }
    context = {'event': event}
    return render(request, 'list.html', context)
