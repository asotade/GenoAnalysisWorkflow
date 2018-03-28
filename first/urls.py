from django.conf.urls import url
from django.contrib.auth import views
from . import views

urlpatterns = [
    url(r'^Login/$', views.user_login, name = "login"),
    url(r'^Logout/$', views.user_logout, name = "logout"),
    url(r'^Home/$', views.home, name = "home"),
    url(r'^Quality score', views.quality, name = "quality"),
    url(r'^Allignment', views.alignment, name = "alignment"),
    url(r'^Variant calling', views.var_calling, name = "var_calling"),
    url(r'^Annotation', views.annotation, name = "annotation"),

    #url(r'^login/$',views.login,name = "login"),
    #url(r'^logout/$',views.logout,name = "logout"),
     #url(r'^logoutin/$',views.logout_then_login,name = "login"),

]
