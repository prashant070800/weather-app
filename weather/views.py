from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer

class WeatherDataView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
