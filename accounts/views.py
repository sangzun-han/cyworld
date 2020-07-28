from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import CyUser, Friend
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            friends = Friend.objects.filter(receiver = request.user, approval = False)
            friends_list = Friend.objects.filter(receiver = request.user, approval = True)|Friend.objects.filter(sender = request.user, approval = True) #sender : 내가 일촌신청한 사람일때 or 내가 허락한 애들
            return render(request,'accounts/index.html',{'friends': friends, 'friends_list': friends_list})
        else :
            return render(request, 'accounts/index.html', {'error' : '이메일이나 비밀번호가 틀렸습니다.',})
    else:
        if request.user.is_authenticated:
            friends = Friend.objects.filter(receiver = request.user, approval = False)
            friends_list = Friend.objects.filter(receiver = request.user, approval = True)|Friend.objects.filter(sender = request.user, approval = True)
            return render(request,'accounts/index.html',{'friends': friends, 'friends_list': friends_list})
        else : 
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

def friend_accept(request):
    friends = Friend.objects.filter(receiver = request.user, approval = False) #아직 허가 안된 일촌
    return render(request,'accounts/friend_accept.html', {'friends': friends})

def friend_detail(request, pk):
    friends = get_object_or_404(Friend, pk = pk)
    return render(request,'accounts/friend_detail.html', {'friends': friends})

def friend_detail_accept(request, pk):
    friends = get_object_or_404(Friend, pk = pk) #객체 있는 애를 friends로 가져옴
    friends.approval = True #받으면
    friends.save() #저장
    return redirect('friend_accept')

def friend_detail_reject(request, pk): #안받은 상태(false)
    friends = get_object_or_404(Friend, pk = pk) 
    friends.delete() #삭제
    return redirect('friend_accept')

def movetofriend(request):
    id = request.GET['tofr']
    url = '/main/index_detail/'+ str(id) #tofr에서 받아온 id 를 붙여줌 /main/index_detail/1 라는 url 생성됨.
    return redirect(url)

def tobefriend(request,pk): #url 통해서 pk 받아오기
    sender = request.user #지금 로그인한사람 (나자신) : 일촌신청한사람
    receiver = get_object_or_404(CyUser,pk = pk) #홈페이지 주인한테 보내는거니까 그사람이 receiver
    url = '/main/index_detail/'+ str(pk) #내가 일촌신청하고싶은 사람 url
    if request.method == 'POST':
        already_f1 = Friend.objects.filter(sender = sender, receiver= receiver) #이미 일촌 상태 보낸사람이 나인 일촌이 이미 존재할때 
        already_f2 = Friend.objects.filter(sender = receiver, receiver= sender) #보낸사람이 받는 사람, 받는사람이 보낸사람인 일촌
        if sender == receiver : #내가 나한테 일촌 신청할때
            return render(request,'accounts/fail.html',{'error': '자신에겐 일촌신청을 할수없습니다.'})
        else : 
            if already_f1: #이미 일촌에 있으면
                return render(request,'accounts/fail.html',{'error': '이미 일촌사이입니다.'})
            elif already_f2: 
                return render(request,'accounts/fail.html',{'error': '이미 일촌사이입니다.'})
            else :
                friends = Friend()
                friends.sender = sender 
                friends.receiver = receiver #페이지 주인
                friends.sender_nickname = request.POST['s_nickname']
                friends.receiver_nickname = request.POST['r_nickname']
                friends.approval = False
                friends.save() 
                return redirect(url)
    return render(request,'accounts/tobefriend.html',{'receiver': receiver}) #post 방식 아닐때(get 방식 아닐 때) 페이지가뜨게하는
