# myProject/myMember/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import UserCreationMultiForm, ProfileForm, ProfileUpdateForm
from django.db.models import Sum
from .models import Profile

def signup(request):
    form = UserCreationMultiForm(request.POST, request.FILES)
    if request.method == 'POST':
        userCheck = request.POST['user-username']
        if request.POST['user-password1'] == request.POST['user-password2']:
            if form.is_valid(): 
                user = form['user'].save()
                profile = form['profile'].save(commit=False)
                profile.user = user
                profile.save()
                print('회원가입 성공')
                return redirect('signin')
            else:
                if User.objects.get(username=userCheck):
                    print('아이디 중복')
                    messages.info(request, '아이디가 중복됩니다.')
                    return render(request, 'signup.html')        
                print('회원가입 실패')
                messages.info(request, '회원가입에 실패했습니다.')
                return render(request, 'signup.html')
        else:
            print('비밀번호가 달라서 실패')
            messages.info(request, '비밀번호가 다릅니다.')
            return render(request, 'signup.html')

    return render(request, 'signup.html', { "form": form })


class Loginviews(LoginView):
    template_name = 'signin.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다. Id 혹은 Password를 확인해 주세요.', extra_tags='danger')
        return super().form_invalid(form)

signin = Loginviews.as_view()


class LogoutViews(LogoutView):
    # setting.py에 설정해준 값
    next_page = settings.LOGOUT_REDIRECT_URL
signout = LogoutViews.as_view()
