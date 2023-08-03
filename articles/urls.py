from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleCommentView,
    ArticleListViewApi,
    ArticleDetailViewApi,
    CommentListViewApi,
    CommentDetailViewApi,
    
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/comments/', ArticleCommentView.as_view(), name='add_comments'),
    #API URLS
    path('articles/', ArticleListViewApi.as_view(), name='article_list_api'),
    path('articles/<int:pk>/', ArticleDetailViewApi.as_view(), name='article_detail_api'),
    path('comments/', CommentListViewApi.as_view(), name='comment_list_api'),
    path('comments/<int:pk>/', CommentDetailViewApi.as_view(), name='comment_detail_api'),
]