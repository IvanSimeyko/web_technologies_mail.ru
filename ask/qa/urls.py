from django.conf.urls import patterns, include, url
from views import index, test, popular, question

urlpatterns = patterns('',
    url(r'^$', index, name='home'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),
    url(r'^popular/', popular, name='popular'),
    url(r'^question/(?P<id>\d+)/$', question, name='question'),
    url(r'^new/', test),
)