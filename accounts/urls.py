from django.urls import path
import accounts.views

urlpatterns = [
    path('',accounts.views.index, name='index'),
    path('signup/',accounts.views.signup, name='signup'),
    path('signup_done/',accounts.views.signup_done, name='signup_done'),
    path('logout/',accounts.views.logout, name='logout'),
    path('friend_accept', accounts.views.friend_accept , name = 'friend_accept'),
    path('friend_detail/<int:pk>', accounts.views.friend_detail, name = 'friend_detail'),
    path('friend_detail_accept/<int:pk>' , accounts.views.friend_detail_accept, name = 'friend_detail_accept'),
    path('friend_detail_reject/<int:pk>' , accounts.views.friend_detail_reject, name = 'friend_detail_reject'),
    path('movetofriend/',accounts.views.movetofriend, name = 'movetofriend'),
    path('tobefriend/<int:pk>', accounts.views.tobefriend, name = 'tobefriend'),
]
