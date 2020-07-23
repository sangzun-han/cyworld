from django.urls import path
import accounts.views

urlpatterns = [
    path('',accounts.views.index, name='index'),
    path('signup/',accounts.views.signup, name='signup'),
    path('signup_done/',accounts.views.signup_done, name='signup_done'),
    path('logout/',accounts.views.logout, name='logout'),

]
