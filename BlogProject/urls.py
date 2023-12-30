from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage),
    path('articles/', include('article.urls')),
    path('user/', include('account.urls')),
    
]
