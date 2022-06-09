from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('add_article/', ArticleCreateView.as_view(), name='add_article'),
    path('add_tag/', TagsCreateView.as_view(), name='add_tag'),
    path('article/<slug:slug_field>/', ArticleDetailView.as_view(), name='one_article'),
    path('tags/', TagsListVies.as_view(),  name='tags'),
    path('login/', LoginUser.as_view(),  name='login'),
    path('register/', RegisterUser.as_view(),  name='register'),
    path('logout/', logout_user,  name='logout'),
    path('tags/<slug:category_slug>', ShowArticleListView.as_view(),  name='article_by_tag'),
]
