"""
URL configuration for django_hw1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
]
=======
    path('', myapp.views.index, name='index'),
    path('login/', myapp.views.login, name="login"),
    path('register/', myapp.views.register, name='register'),
    path('main/', myapp.views.main, name='main'),
    path('blog/', myapp.views.blog_detail, name='blog_detail'),
    path('create_blog', myapp.views.create, name='create_blog')
    ]
>>>>>>> f671637 (HW2)
