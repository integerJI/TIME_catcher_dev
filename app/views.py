from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from .models import Timesave
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Sum


def index(request):
    return render(request, 'index.html')

def subpage(request):
    return render(request, 'subpage.html')
