from django.urls import path

from . import views

app_name = 'branch'

urlpatterns = [
    path('', views.branchs, name='branchs'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.branch, name='branch'),
    path('<uuid:pk>/update', views.update, name='update'),
    path('<uuid:pk>/delete', views.delete, name='delete'),
]