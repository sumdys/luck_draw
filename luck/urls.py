"""luck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from draw import views as luck_draw

urlpatterns = [
    url(r'^$',luck_draw.index),
    url(r'^get_first_prize/$',luck_draw.get_first_prize),
    url(r'^get_second_prize/$',luck_draw.get_second_prize),
    url(r'^get_third_prize/$',luck_draw.get_third_prize),
    url(r'^get_prize/$',luck_draw.get_prize),
    url(r'^add/$',luck_draw.add),
    url(r'^person/$',luck_draw.person),
    url(r'^admin/', admin.site.urls),
]
