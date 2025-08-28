import requests
from .models import WeatherData

URL = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt"

def fetch_and_store_weather_data():
    response = requests.get(URL)
    if response.status_code != 200:
        return

    lines = response.text.splitlines()
    for line in lines[7:]:  # skip header
        parts = line.split()
        if len(parts) >= 13:
            year = int(parts[0])
            monthly_values = parts[1:13]
            for month, val in enumerate(monthly_values, start=1):
                WeatherData.objects.update_or_create(
                    year=year, month=month,
                    defaults={"value": float(val) if val != "---" else None}
                )
