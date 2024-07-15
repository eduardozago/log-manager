from django.urls import path

from . import views

app_name = 'vehicle'

urlpatterns = [
    path('', views.vehicles, name='vehicles'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.vehicle, name='vehicle'),
    path('<uuid:pk>/update', views.update, name='update'),
    path('<uuid:pk>/delete', views.delete, name='delete'),
]