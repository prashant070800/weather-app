from django.db import models

class WeatherData(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    value = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("year", "month")

    def __str__(self):
        return f"{self.year}-{self.month}: {self.value}"
