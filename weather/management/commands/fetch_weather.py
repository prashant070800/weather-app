from django.core.management.base import BaseCommand
from weather.utils import fetch_and_store_weather_data

class Command(BaseCommand):
    help = "Fetch and store weather data from UK MetOffice"

    def handle(self, *args, **kwargs):
        fetch_and_store_weather_data()
        self.stdout.write(self.style.SUCCESS("Weather data fetched successfully!"))
