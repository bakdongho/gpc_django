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
# from django.contrib.auth.views import LogoutView
# from boards.views import ArticleCreateUpdateView, ArticleDetailView, ArticleListView, hello_world
# from user.views import UserRegistrationView, UserLoginView, UserVerificationView, ResendVerifyEmailView
from boards.views import ArticleListView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view()),

    path('article/', include(('boards.urls','boards'))),

    path('user/', include(('user.urls','user'))),

]
