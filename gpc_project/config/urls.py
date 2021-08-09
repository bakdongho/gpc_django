"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boards.views import ArticleCreateUpdateView, ArticleDetailView, ArticleListView, hello_world
from user.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<to>', hello_world, name='hello'),

    path('article/', ArticleListView.as_view(), name='list_article'),
    path('article/create/', ArticleCreateUpdateView.as_view(),name='create_or_update_article'),
    path('article/<article_id>/', ArticleDetailView.as_view(), name='detail_article'),
    path('article/<article_id>/update/', ArticleCreateUpdateView.as_view(), name='create_or_update_article'),

    path('user/create/', UserRegistrationView.as_view()),
]
