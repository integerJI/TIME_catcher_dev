from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('subpage/', views.subpage, name='subpage'),
]
