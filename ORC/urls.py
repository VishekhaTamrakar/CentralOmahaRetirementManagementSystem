from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as RestaurantBlog_views
from django.contrib.auth import views as auth_views
app_name = 'ORC'
urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    url(r'^signup/$', RestaurantBlog_views.signup, name='signup'),
    ]