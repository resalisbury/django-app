from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^polls/api/v1/', include('polls.api_urls', namespace="polls_api")),
    url(r'^admin/', include(admin.site.urls)),
)
