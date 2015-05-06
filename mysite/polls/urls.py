from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns(
    '',
    url(r'^export$', views.export, name='index'),
    url(r'^$', views.IndexView.as_view(), name='export'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
