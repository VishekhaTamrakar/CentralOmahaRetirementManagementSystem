from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as ORC_views
from django.contrib.auth import views as auth_views
app_name = 'ORC'
urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    url(r'^signup/$', ORC_views.signup, name='signup'),
    path('workorder_list', views.workorder_list, name='workorder_list'),
    path('workorder/<int:pk>/edit/', views.workorder_edit, name='workorder_edit'),
    path('workorder/<int:pk>/delete/', views.workorder_delete, name='workorder_delete'),
    path('workorder/new/', views.workorder_new, name='workorder_new'),


    ]