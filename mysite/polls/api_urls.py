from django.conf.urls import patterns, url

from polls import api_views

urlpatterns = patterns(
    '',
    url(r'^questions/$', api_views.QuestionList.as_view(), name="question_rest_api"),
    url(r'^choices/$', api_views.ChoiceList.as_view(), name="question_rest_api"),
)
