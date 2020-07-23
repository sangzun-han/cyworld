from django.shortcuts import render, redirect
from django.contrib import auth
from .models import CyUser
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else :
            return render(request, 'accounts/index.html', {'error' : '이메일이나 비밀번호가 틀렸습니다.'})
    else:
        return render(request,'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['passwd1'] == request.POST['passwd2']:
            name = request.POST['name']
            user = CyUser.objects.create_user(
                username=request.POST['username'],
                password=request.POST['passwd1'],
                email = request.POST['email'],
                birth = request.POST['birth'],
                full_name = name,
                title = name + '님의 미니홈피',
                sex = request.POST['sex'],
                today = 0, 
                total = 0,
            )
            return redirect('signup_done')
        return render(request,'singup.html',{'error': '비밀번호가 틀립니다.'})
    return render(request,'accounts/signup.html')

def signup_done(request):
    return render(request, 'accounts/signup_done.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
