from django.urls import path
from main.views import *
urlpatterns = [
    path(r"",user_sign,name="user_sign"),
    path('setcookies/',setcookie,name="setcookies"),
    path('setcookie1/',setcookie1,name="setcookies1"),
    path('getcookie1/',getcookie1,name="getcookies1"),
    path('delcookie1/',delcookie1,name="delcookies1"),
    # path(r"user_login",user_login,name="user_login"),
]
