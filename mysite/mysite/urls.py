from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^api/v1/polls/', include('polls.api_urls', namespace="polls_api")),
    url(r'^api/v1/chat/', include('chat.api_urls', namespace="chat_api")),
    url(r'^admin/', include(admin.site.urls)),
)
