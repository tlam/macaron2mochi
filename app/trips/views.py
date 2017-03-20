from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from trips.models import Trip


def index(request):
    trips = Trip.objects.all()
    data = {
        'trips': []
    }
    for trip in trips:
        data['trips'].append({
            'id': trip.pk,
            'name': trip.name,
            'itineraries_url': '/trips/{}/itineraries'.format(trip.pk)
        })
    return JsonResponse(data)


def itineraries(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)
    data = {
        'itineraries': [],
        'name': trip.name
    }
    date_format = '%a, %b %d'
    time_format = '%H:%M'
    itineraries = []
    for itinerary in trip.itineraries.all():
        activities = []
        for activity in itinerary.activities.all():
            activities.append({
                'id': activity.id,
                'name': activity.name,
                'description': activity.description,
                'icon': activity.category.icon,
                'start_time': activity.start_time.strftime(time_format),
                'end_time': activity.end_time.strftime(time_format),
                'url': reverse('admin:activities_activity_change', args=(activity.pk,))
            })

        itineraries.append({
            'id': itinerary.id,
            'name': itinerary.name,
            'description': itinerary.description,
            'date': itinerary.date.strftime(date_format),
            'activities': activities,
        })
        if len(itineraries) == 6:
            data['itineraries'].append(itineraries)
            itineraries = []

    if itineraries:
        data['itineraries'].append(itineraries)

    return JsonResponse(data)
