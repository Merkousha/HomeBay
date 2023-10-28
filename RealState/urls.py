from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static 
from django.conf import settings  
from django.contrib import admin
from .views import list,detail


urlpatterns = [
    path('', list , name='list'),
    path('detail/<int:pk>/', detail , name='detail'),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)