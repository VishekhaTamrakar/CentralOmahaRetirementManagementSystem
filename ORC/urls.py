from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as ORC_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'ORC'
urlpatterns = [

    path('', views.about, name='about'),
    re_path(r'^home/$', views.about, name='home'),
    url('about/', views.about, name='about'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('ORC:password_reset_done')),
         {'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^signup/$', ORC_views.signup, name='signup'),
    url('workorder_list/', views.workorder_list, name = 'workorder_list'),
    url('property_list/', views.property_list, name='property_list'),
    url('resident_list/', views.resident_list, name='resident_list'),
    url('maintenacework_list/', views.maintenancework_list, name='maintenancework_list'),
    url('maintenance_worker_list/', views.maintenance_worker_list, name='maintenance_worker_list'),
    url('staff_list/', views.staff_list, name='staff_list'),





]