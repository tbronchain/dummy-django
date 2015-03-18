from django.conf.urls import patterns, url
from dummypoll import views

urlpatterns = patterns(
    '',
#    url(r'^$', views.index, name='index'),
#    # ex: /dummypoll/5/
#    url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name='detail'),
#    # ex: /dummypoll/5/results/
#    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /dummypoll/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
)
