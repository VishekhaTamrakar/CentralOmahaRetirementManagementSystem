from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as RestaurantBlog_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'ORC'
urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    url(r'^signup/$', RestaurantBlog_views.signup, name='signup'),
    url('about/',views.about, name='about'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('ORC:password_reset_done')),
         {'email_template_name': 'ORC/password_reset_email.html'}, name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='ORC/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='ORC/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='ORC/password_reset_complete.html'),name='password_reset_complete'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password/$', views.change_password, name='change_password'),
    ]