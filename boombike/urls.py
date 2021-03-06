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
#    url(r'^404$', 'info.views.page_not_found', name='page_not_found'),
    # Translation
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {
     'sitemaps': sitemaps,
     'template_name': 'info/custom_sitemap.html'},),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     # Albums
     url(_(r'^albums$'), 'info.views.albums', name='albums'),

     # Facebook all auth
     (r'^accounts/', include('allauth.urls')),

)

urlpatterns += i18n_patterns('',
    url(_(r'^$'), 'info.views.home', name='home'),
    url(_(r'^bicycle-touring$'), 'info.views.bicycle_touring', name='bicycle-touring'),
    url(_(r'^boom-festival$'), 'info.views.boom_festival', name='boom-festival'),
    url(_(r'^boom-and-bike$'), 'info.views.boom_and_bike', name='boom-and-bike'),
    url(_(r'^get-there$'), 'info.views.get_there', name='get-there'),
    url(_(r'^together$'), 'info.views.together', name='together'),
    url(_(r'^get-there$'), 'info.views.get_there', name='get-there'),
    url(_(r'^city_visit/(?P<location>.+)$'), 'info.views.city_visit', name='city_visit'),
    url(_(r'^user_checkpoints/(?P<id>[0-9]+)$'), 'info.views.user_checkpoints', name='user_checkpoints'),
)

#urlpatterns += patterns('django.contrib.auth.views',
#    (_(r'^accounts/login/$'),  'login'),
#    (_(r'^accounts/logout/$'), 'logout'),
#)

handler404 = 'info.views.page_not_found'
