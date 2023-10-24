from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from .models import Property

def list(request):
    properties = Property.objects.all() #Read All Properties from Database
    return render(request, 'list.html',{'properties': properties})

def detail(request,pk=None):
    property = get_object_or_404(Property , pk=pk)
    return render(request, 'detail.html',{'property': property})
    

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

