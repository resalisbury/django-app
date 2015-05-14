from django.conf.urls import patterns, url

from chat import api_views

urlpatterns = patterns(
    '',
    url(r'^$', api_views.ChatList.as_view(), name="chat_rest_api"),
    url(r'^v(?P<version>\d+\.?\d{1,2})$', api_views.ChatDetail.as_view(), name="chat_rest_api"),
)
