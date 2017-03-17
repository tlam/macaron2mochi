from django.http import JsonResponse
from django.shortcuts import render

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
            'itineraries': '/trips/{}/itineraries'.format(trip.pk)
        })
    return JsonResponse(data)


def itineraries(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)
    data = {
        'itineraries': []
    }
    for itinerary in trip.itineraries.all():
        activities = []
        for activity in itinerary.activities.all():
            activities.append({
                'id': activity.id,
                'name': activity.name,
                'description': activity.description,
                'start_time': activity.start_time,
                'end_time': activity.end_time
            })
        data['itineraries'].append({
            'id': itinerary.id,
            'name': itinerary.name,
            'date': itinerary.date,
            'activities': activities
        })
    return JsonResponse(data)
