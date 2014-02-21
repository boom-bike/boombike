from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'info.views.home', name='home'),
    url(r'^home_details/$', 'info.views.home_details', name='home_details'),

    url(r'^bicycle_touring/$', 'info.views.bicycle_touring', name='bicycle_touring'),
    url(r'^boom_festival/$', 'info.views.boom_festival', name='boom_festival'),
    url(r'^boom_and_bike/$', 'info.views.boom_and_bike', name='boom_and_bike'),

    # Translation
    (r'^i18n/', include('django.conf.urls.i18n')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
