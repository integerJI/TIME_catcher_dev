from django.urls import path
from . import views

urlpatterns = [
    path('timesave/', views.timesave, name='timesave'),
]
