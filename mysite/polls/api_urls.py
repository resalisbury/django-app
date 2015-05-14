from django.conf.urls import patterns, url

from polls import api_views

urlpatterns = patterns(
    '',
    url(r'^$', api_views.QuestionList.as_view(), name="question_rest_api"),
)
