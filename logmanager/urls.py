"""
URL configuration for logmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('account.urls')),
    path('branchs/', include('branch.urls')),
    path('trips/', include('trip.urls')),
    path('vehicles/', include('vehicle.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

def custom_page_not_found_view(request, exception):
    return render(request, 'core/404.html', {}, status=404)

def custom_error_view(request):
    return render(request, 'core/500.html', status=500)

handler404 = custom_page_not_found_view
handler500 = custom_error_view
