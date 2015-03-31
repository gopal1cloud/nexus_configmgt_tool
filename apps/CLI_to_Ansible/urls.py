from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('apps.CLI_to_Ansible.views',
    url(r'^$', 'main'), 
    url(r'^convert/$', 'convert'), 
)
