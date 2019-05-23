"""whatevs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from events_manager import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name='events_manager-home'),
    path('events_manager/', views.events, name='events_manager-events_manager'),
    path('new_event/', views.new_event, name='events_manager-new_event'),
    path('new_activity/', views.new_activity, name='events_manager-new_activity'),
]

