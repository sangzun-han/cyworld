from django.urls import path
import main.views
#미디어 파일 사용을 위해

urlpatterns = [
    path('main',main.views.index , name='main'),
    path('guest/',main.views.guest, name='guest'),
    path('diary/',main.views.diary, name='diary'),
    path('profile/', main.views.profile, name='profile'),
    path('picture/',main.views.picture, name='picture'),
    path('updateProfile/',main.views.updateProfile, name='updateProfile'),
    path('updateTitle/',main.views.updateTitle, name='updateTitle'),
]

