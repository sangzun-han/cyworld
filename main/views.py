from django.shortcuts import render,redirect, get_object_or_404 #객체 있으면 ㅇㅋ
from accounts.models import CyUser,Friend
from . models import Guestbook,Friendsay,Diary
# Create your views here.

def index(request):
    friendsay = Friendsay.objects.all() #일촌평 전부
    friends_list = Friend.objects.filter(receiver = request.user, approval = True)|Friend.objects.filter(sender = request.user, approval = True) #나와 일촌인사람
    return render(request,'main/index.html',{
        'friendsay':friendsay,
        'friends_list':friends_list,
    })

def guest(request):
    guestbook = Guestbook.objects.filter(receiver_name = request.user)
    return render(request,'main/guest.html',{
        'guestbook':guestbook
    })

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
    
def search(request):
    search = request.GET['search_name']
    cyuser = CyUser.objects.all() 
    if search:
        cyusers = cyuser.filter(full_name__icontains = search)
        return render(request, 'main/search_list.html', {
            'cyusers' : cyusers #cyuser라는 변수를 cyuser라는 이름으로 보낼거다.
        })
def index_detail(request, pk):
    sender = request.user #지금 로그인한사람 (나자신) : 일촌신청한사람
    receiver = get_object_or_404(CyUser,pk = pk) #홈페이지 주인한테 보내는거니까 그사람이 recever
    friends_list = Friend.objects.filter(sender = sender, receiver= receiver) | Friend.objects.filter(sender = receiver, receiver= sender) #일촌이라면
    friendsay = Friendsay.objects.all()
    cyuser = get_object_or_404(CyUser, pk = pk)
    return render(request, 'main/index_detail.html', {
        'cyuser' : cyuser,
        'friends_list':friends_list,
        'friendsay':friendsay
        })

def guest_detail(request,pk):
    sender = request.user
    cyuser = get_object_or_404(CyUser,pk=pk)
    guestbook = Guestbook.objects.filter(receiver_name = cyuser)
    receiver = get_object_or_404(CyUser,pk=pk)
    friends_list = Friend.objects.filter(sender = sender, receiver= receiver) | Friend.objects.filter(sender = receiver, receiver= sender) #일촌이라면

    if request.method == 'POST':
        guestname = request.user
        guesttext = request.POST['guest_text']

        guestbooks = Guestbook()

        guestbooks.guestname = guestname
        guestbooks.guest_text = guesttext
        guestbooks.receiver_name = cyuser
        guestbooks.save()
        return render(request, 'main/guest_detail.html',{
            'guestbook':guestbook,
            'cyuser':cyuser,
            'friends_list':friends_list
        })
    else:
        return render(request, 'main/guest_detail.html',{
            'guestbook':guestbook,
            'cyuser':cyuser
        })
    


def friendsay(request,pk):
    receiver = get_object_or_404(CyUser,pk=pk)

    if request.method == 'POST':
        friendname = request.user
        friendsay = request.POST['friendsay']
        receiver_name = receiver

        friend_say = Friendsay()

        friend_say.friend_name = friendname
        friend_say.friend_say = friendsay
        friend_say.receiver_name = receiver_name
        
        friend_say.save()
        return redirect('main')
    else:
        return redirect('main')

def diary_detail(request,pk):
    cyuser = get_object_or_404(CyUser,pk=pk)
    diary = Diary.objects.filter(receiver_name=cyuser)
    return render(request,'main/diary_detail.html',{
        'cyuser':cyuser,
        'diary':diary
    })

def diary_create(request,pk):
    cyuser = get_object_or_404(CyUser,pk=pk)
    diary = Diary.objects.filter(receiver_name=cyuser)
    if request.method == 'POST':

        diarys = Diary()
        diary_title = request.POST['diary_title']
        diary_say = request.POST['diary_say']

        diarys.diary_title = diary_title
        diarys.diary_say = diary_say
        diarys.diary_name = cyuser
        diarys.receiver_name = cyuser
        diarys.save()

        return render(request, 'main/diary_detail.html',{
            'cyuser':cyuser,
            'diary':diary
        })
    else: #작성이 안됐다?
        return render(request,'main/diary_create.html',{
            'cyuser':cyuser
        })