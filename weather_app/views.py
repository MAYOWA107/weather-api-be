from django.core.cache import cache
from django.shortcuts import render
from .service import get_weather_data


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class WeatherView(APIView):
    def get(self, request, city):
        cache_key = f"weather:{city.lower()}"

        cached_data = cache.get(cache_key)
        if cached_data:
            print("Cache Hit")
            return Response(cached_data)

        print("Cache missed")
        data = get_weather_data(city)

        if data is None:
            return Response(
                {"error": "Failed to fetch weather"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        cache.set(cache_key, data, timeout=60 * 60 * 12)
        return Response(data)
