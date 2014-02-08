from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import AllVulnsListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pwnhub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'(/.*)?$', AllVulnsListView.as_view(template_name="all_vulns.html")),
)