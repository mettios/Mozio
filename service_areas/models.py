from django.db import models
from djgeojson.fields import PolygonField
from providers.models import Provider


class ServiceArea(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00, blank=False, null=False)
    polygon = PolygonField(blank=True, null=True)
    # provider = models.ForeignKey(Provider, related_name='service_areas', on_delete=models.CASCADE)
