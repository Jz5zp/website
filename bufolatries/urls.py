"""bufolatries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.urls import path, re_path, include
from adoptions import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login, name='login'),
    path('comment/', include('comment.urls')),
    path('register/', views.register, name='register'),
    path('reference/', views.reference, name='refer'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about us'),
    re_path(r'^adoptions/(\d+)', views.blog_detail, name='blog_detail'),
    path('ckeditor', include('ckeditor_uploader.urls')),
]
