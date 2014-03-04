from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from sitemaps import ViewSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'views_sitemap': ViewSitemap,
}

urlpatterns = patterns('',
    # Translation
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {
     'sitemaps': sitemaps,
     'template_name': 'info/custom_sitemap.html'},),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(_(r'^$'), 'info.views.home', name='home'),
    url(_(r'^bicycle-touring$'), 'info.views.bicycle_touring', name='bicycle-touring'),
    url(_(r'^boom-festival$'), 'info.views.boom_festival', name='boom-festival'),
    url(_(r'^boom-and-bike$'), 'info.views.boom_and_bike', name='boom-and-bike'),
)

#handler404 = 'boombike.views.handler404'
