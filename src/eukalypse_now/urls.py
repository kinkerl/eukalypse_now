from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eukalypse_now.views.home', name='home'),
    url(r'^testrun/list/', 'eukalypse_now.views.testrun_list'),
    url(r'^testrun/detail/(?P<testrun_id>\d+)/', 'eukalypse_now.views.testrun_detail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static2/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.TWITTER_BOOTSTRAP_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'eukalypse_now.views.testrun_list'),
)
