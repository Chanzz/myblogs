from . import views
from django.urls import path

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.detail, name='article_detail'),
    path('article-create/', views.create, name='article_create'),
    path('article-delete/<int:id>/', views.delete, name='article_delete'),
    path('article-update/<int:id>/', views.updata, name='article_updata'),
]
app_name = '[article]'
