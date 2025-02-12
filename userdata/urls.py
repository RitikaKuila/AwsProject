from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('test/',views.home ),
    path('calci/',views.calculator),
    path('',views.landingPage),
    path('userform/',views.userdata,name='userform'),
    path('fetchdata/',views.fetchdata_user_all,name='fetchdata'),
    path('update_userdata/',views.update_userdata,name='update_userdata'),
    path('deleteuserdata/',views.deleteuserdata,name='deleteuserdata'),
]