from django.urls import path
from .views import ArticleCreateUpdateView, ArticleDetailView, ArticleListView

urlpatterns = [

    path('', ArticleListView.as_view(), name='listArticle'),
    path('create', ArticleCreateUpdateView.as_view(),name='createArticle'),
    path('<article_id>', ArticleDetailView.as_view(), name='detailArticle'),
    path('<article_id>/update', ArticleCreateUpdateView.as_view(), name='updateArticle'),
]