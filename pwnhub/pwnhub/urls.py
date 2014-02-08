from django.conf.urls import patterns, include, url
from django.contrib import admin
import vulns.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pwnhub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vulns/', include(vulns.urls)),
)