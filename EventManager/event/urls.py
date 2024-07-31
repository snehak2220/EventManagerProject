
from django.urls import path

from event import views

urlpatterns = [

    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('team', views.viewteam, name='team'),
    path('profile',views.profile,name='profile'),
    path('book',views.bookevent,name='book')
]
