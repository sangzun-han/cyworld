from django.shortcuts import render,redirect
from accounts.models import CyUser
# Create your views here.

def index(request):
    return render(request,'main/index.html')

def guest(request):
    return render(request,'main/guest.html')

def diary(request):
    return render(request,'main/diary.html')

def profile(request):
    return render(request,'main/profile.html')

def picture(request):
    return render(request,'main/picture.html')

def updateProfile(request):
    if request.method == 'POST' and 'imgs' in request.FILES:
        user = request.user
        contents = request.POST['contents']
        imgs = request.FILES['imgs']
        user.profile_img = imgs
        user.contents = contents
        user.save()
        return render(request,'main/updateProfile.html', {'done':'사진과 소개가 업데이트 되었습니다.'})
    elif request.method == 'POST':
        user = request.user
        contents = request.POST['contents']
        user.contents = contents
        user.save()
        return render(request,'main/updateProfile.html', {'done':'소개가 업데이트 되었습니다.'})
    return render(request,'main/updateProfile.html')

def updateTitle(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        user.title = title
        user.save()
        return redirect('index')
    else:
        return render(request,'main/index.html')
    
