#urls.py
from django.conf.urls import url


from . import views



urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    url(r'users/', views.userProfile, name='userProfile'),
    url(r'like/', views.FavLike, name='FavLike'),

    url(r'userView/', views.userView, name='userView'),




    url(r'addWord/', views.addWord, name='addWord'),
    url(r'createUser/', views.createUser, name='createUser'),
    url(r'loggedout/', views.loggedout, name='loggedout'),
    url(r'logging/', views.logging, name='logging'),




    url(r'', views.index, name='index'),
    ]

