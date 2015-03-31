from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'', include('apps.CLI_to_Ansible.urls')), 
    url(r'^admin/', include(admin.site.urls)),
)
