from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from .models import Timesave

# Create your views here.

def index(request):
    return render(request, 'index.html')


def timesave(request):
    timesave = Timesave()
    timesave.save_user = User.objects.get(username = request.user.get_username())
    timesave.save_date = request.GET.get('time')
    print("aaaaaaaaaaaaaaa")
    print(timesave.save_date)
    print("aaaaaaaaaaaaaaa")
    timesave.save()
    return redirect(reverse('index'))