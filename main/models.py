from django.db import models
from accounts.models import CyUser
# Create your models here.

class Guestbook(models.Model):
    guestname = models.ForeignKey(CyUser, on_delete = models.CASCADE, related_name='guestname')
    receiver_name = models.ForeignKey(CyUser, on_delete=models.CASCADE, related_name = 'receive_name')
    guest_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #최초 저장시에만 생성
    updated_at = models.DateTimeField(auto_now=True) #최종수정일자

class Friendsay(models.Model):
    friend_name = models.ForeignKey(CyUser, on_delete=models.CASCADE, related_name = 'friend_name')
    receiver_name = models.ForeignKey(CyUser, on_delete=models.CASCADE, related_name = 'receiver_name')
    friend_say = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #최초 저장시에만 생성
    updated_at = models.DateTimeField(auto_now=True) #최종수정일자