from django.urls import path, re_path
from django.views.generic import RedirectView

# importing views from app
from . import views

# Create your views here.
urlpatterns = [
    path('', views.articles_list, name='articles_list'),  # Set the homepage to articles_list
    path('create_article/', views.create_article, name='create_article'), # for creating new article
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
    re_path(r'^.*/$', RedirectView.as_view(url='/articles/', permanent=False)),
    
]