from __future__ import unicode_literals

from django.db import models


class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    date = models.DateField()
    trip = models.ForeignKey('trips.Trip', on_delete=models.CASCADE, related_name='itineraries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return u'{}'.format(self.name)

