from django.urls import path, re_path
from django.views.generic import RedirectView

# importing views from app
from . import views

# Create your views here.
urlpatterns = [
    path('login/', views.user_login, name='user_login'), 
    path('logout/', views.user_logout, name='user_logout'), 
    path('registeration/', views.user_register, name='user_register'), # for registering new user
    path('success/', views.success_message_view, name='success_message_view'),
    path('profile/', views.view_user_profile, name='user_profile'),
    re_path(r'^.*/$', RedirectView.as_view(url='/articles/', permanent=False)),
]