#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

class ViewSitemap(Sitemap):
    """Reverse static views for XML sitemap."""

    changefreq = 'monthly'

    def items(self):
        # Return list of url names for views to include in sitemap
        return [ 'home',
                 'bicycle-touring',
                 'boom-festival',
                 'boom-and-bike',
                 'get-there',
                ]

    def location(self, item):
        return reverse(item)

