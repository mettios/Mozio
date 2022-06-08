from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from .models import ServiceArea


class ServiceAreaSerializer(GeoModelSerializer):
    # provider_name = serializers.RelatedField(source='provider', read_only=True)

    class Meta:
        model = ServiceArea
        geo_field = 'polygon'
        fields = [
            'name',
            'price',
            'polygon'
        ]
