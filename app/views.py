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

def index(request):
    return render(request, 'index.html')

@login_required
@require_POST
def timesave(request):
    if request.method == 'POST':
        timesave = Timesave()
        timesave.save_user = User.objects.get(username = request.user.get_username())
        timesave.save_date = request.POST.get('time')
        print("aaaaaaaaaaaaaaa")
        print(timesave.save_date)
        print("aaaaaaaaaaaaaaa")
        timesave.save()
        context = {'time' : timesave.save_date}
        return HttpResponse(json.dumps(context), content_type='application/json')

# @login_required
# @require_POST
# def like(request):
#     if request.method == 'POST':
#         user = request.user 
#         create_user = request.POST.get('pk', None)
#         post = get_object_or_404(Post, id=create_user)

#         if post.post_likes.filter(id = user.id).exists():
#             post.post_likes.remove(user) 
#             message = '좋아요 취소'
#         else:
#             post.post_likes.add(user)
#             message = '좋아요!'

#     context = {'likes_count' : post.total_likes, 'message' : message}
#     return HttpResponse(json.dumps(context), content_type='application/json')