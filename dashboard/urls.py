"""dashboard URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from django import urls

from pages import views
from pages import urls as pages_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pages/', include('pages.urls'))
    # re_path(r'index$', views.index, name='index'),
    # # re_path(r"browse$", views.browse, name='browse'),
    # re_path(r'^browse$', views.browse, name='browse'),
    # re_path(r"^browse_results$", views.browse_results, name='browse_results'),
    # re_path(r"search$", views.search, name='search'),
    # re_path(r"help$", views.help, name='help')
]
