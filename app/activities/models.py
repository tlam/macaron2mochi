from __future__ import unicode_literals

from django.db import models


class Activity(models.Model):
    CURRENCIES = (
        ('CAD', 'CAD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('JPY', 'JPY'),
        ('KRW', 'KRW'),
        ('USD', 'USD'),
    )

    itinerary = models.ForeignKey('itineraries.Itinerary', on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    directions = models.TextField(default='', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='', blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    address = models.CharField(max_length=255, default='', blank=True)
    city = models.CharField(max_length=255, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_time']

    def __unicode__(self):
        return u'{}'.format(self.name)
