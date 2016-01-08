from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'ssdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('movies.urls')),
    url(r'^api/register/$', 'authentication.views.register'),
    url(r'^api/login/$', 'authentication.views.login'),
    url(r'^api/logout/$', 'authentication.views.logout'),
]
