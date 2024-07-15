from django.urls import path

from . import views

app_name = 'trip'

urlpatterns = [
    path('', views.trips, name='trips'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.trip, name='trip'),
    path('<uuid:pk>/completed', views.completed, name='completed'),
    path('<uuid:pk>/update', views.update, name='update'),
    path('<uuid:pk>/delete', views.delete, name='delete'),
]