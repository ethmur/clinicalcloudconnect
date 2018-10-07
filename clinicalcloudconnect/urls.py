"""clinicalcloudconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
	re_path(r'^$', views.index),
	re_path(r'^user(?P<pk>\d+)/$', views.user_detail),
	re_path(r'^user(?P<pk>\d+)/upload-file$', views.user_upload_file),
	re_path(r'^user(?P<pk>\d+)/post-file$', views.user_post_file),
	re_path(r'^user(?P<pk>\d+)/add-hp$', views.user_add_hp),
	re_path(r'^user(?P<pk>\d+)/post-add-hp$', views.user_post_add_hp),
	re_path(r'^hp(?P<pk>\d+)/$', views.hp_detail),
	re_path(r'^hp(?P<pk>\d+)/user(?P<upk>\d+)/$', views.hp_user_detail),
	re_path(r'^hp(?P<pk>\d+)/user(?P<upk>\d+)/upload-file$', views.hp_user_upload_file),
	re_path(r'^hp(?P<pk>\d+)/user(?P<upk>\d+)/post-file$', views.hp_user_post_file),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
