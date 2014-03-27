from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cbgrandslam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^backend/', include(admin.site.urls)),

    url(r'^$', 'game.views.home', name='home')

)
