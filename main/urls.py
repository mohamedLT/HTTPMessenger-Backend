from django.urls import path
from . import views
from .models import *


urlpatterns = [
    path('list/', views.get_list ,name="list"),
    path('active/', views.get_active ,name="active"),
    path('addmsg',views.add_message,name="msg"),
    path('user',views.add_user,name="user"),
    path('check',views.check_user,name="check"),
    path('getmsg',views.fetch_msgs,name="getmsg")

]