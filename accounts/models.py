from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class CyUser(AbstractUser):
    email = models.EmailField(max_length=50)
    sex = models.CharField(max_length = 10, null = True)
    birth = models.DateField(null = True)
    title = models.TextField(null = True)
    today = models.IntegerField(null = True)
    total = models.IntegerField(null = True)
    profile_img = models.ImageField(null = True, upload_to="%Y/%m/%d")
    today_f = models.TextField(null = True)
    full_name = models.CharField(max_length = 30, null = True)
    contents = models.TextField(null = True)

    profile_title = models.CharField(max_length=255, null=True)
    profile_content = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return self.full_name
    
    @property #템플릿 안에서 이 함수를 쓰겠다.
    def today_fnc(self):  
        today = datetime.today().strftime("%Y-%m-%d")
        if self.today_f != today:#오늘이랑 어제랑 다르면
            self.today_f = today  #오늘 날짜를 todayf 로 넣고
            self.today = 0 #초기화
            self.today += 1
            self.total += 1
            self.save()
        
        else : 
            self.today += 1
            self.total += 1
            self.save()

class Friend(models.Model):
    sender = models.ForeignKey(CyUser, on_delete = models.CASCADE, related_name = 'sender')
    receiver = models.ForeignKey(CyUser, on_delete = models.CASCADE, related_name = 'receiver')
    sender_nickname = models.CharField(blank=True, max_length=50)
    recever_nickname = models.CharField(blank=True, max_length=50)
    approval = models.BooleanField()

    def __str__(self):
        return self.sender.full_name+'님과'+self.recever.full_name+"님의 일촌관계"
        


