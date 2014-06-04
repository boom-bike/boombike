from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

FRANCE_COUNTRY_NAME = u'France'
SPAIN_COUNTRY_NAME = u'Spain'
PORTUGAL_COUNTRY_NAME = u'Portugal'

COUNTRY_CHOICES = ( (FRANCE_COUNTRY_NAME, FRANCE_COUNTRY_NAME),
                    (SPAIN_COUNTRY_NAME, SPAIN_COUNTRY_NAME),
                    (PORTUGAL_COUNTRY_NAME, PORTUGAL_COUNTRY_NAME)
)

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=8)
    country = models.CharField(max_length=64, choices=COUNTRY_CHOICES)

    def __unicode__(self):
        return '%s - %s - %s' % (self.name, self.zip_code, _(self.country))

    class Meta:
        verbose_name = u'City'
        ordering = ('name',)
        verbose_name_plural = u'Cities'
        unique_together = ('name', 'zip_code', 'country')

class CityVisit(models.Model):
    user = models.ForeignKey(User)
    location = models.CharField(max_length=256)
    date = models.DateField()

    class Meta:
        ordering = ('date', )
        verbose_name = _('Checkpoint')
        verbose_name_plural = _('Checkpoints')
