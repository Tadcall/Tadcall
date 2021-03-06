"""tadcall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import backend.work

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_user/', backend.work.get_user),
    url(r'^get_links/', backend.work.get_links),
    url(r'^add_real_phone_number/', backend.work.add_real_phone_number),
    url(r'^get_real_phone_numbers/', backend.work.get_real_phone_numbers),
    url(r'^get_virtual_phone_numbers/', backend.work.get_virtual_phone_numbers),
    url(r'^delete_real_phone_number/', backend.work.delete_real_phone_number),
    url(r'^add_link/', backend.work.add_link),
    url(r'^add_link_with_restrictions/', backend.work.add_link_with_restrictions),
    url(r'^answer/', backend.work.answer)
]
