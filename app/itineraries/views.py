from django.http import JsonResponse
from django.shortcuts import render

from itineraries.models import Itinerary


def index(request, trip_id):
    itineraries = Itinerary.objects.filter(trip=trip_id)
    data = {
        'itineraries': []
    }
    return JsonResponse(data)



