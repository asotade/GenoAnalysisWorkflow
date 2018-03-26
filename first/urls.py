from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$',views.user_login,name = "login"),
    url(r'^logout/$',views.user_logout,name = "logout"),
    url(r'^home/$',views.home,name = "home"),

    #url(r'^login/$',django.contrib.auth.views.login,name = "login"),
    #url(r'^logout/$',django.contrib.auth.views.logout,name = "logout"),
    #url(r'^logoutin/$',django.contrib.auth.views.logout_then_login,name = "login"),

]
