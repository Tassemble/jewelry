from django.conf.urls import patterns, url, include

from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wellpearl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
