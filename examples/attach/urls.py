from django.conf.urls import url, include
from attach.attacher.views import index
from attach import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [url(r'^$', index),]
