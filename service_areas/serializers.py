from rest_framework import serializers
# from rest_framework_gis.serializers import GeoModelSerializer
from .models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    # provider_name = serializers.RelatedField(source='provider', read_only=True)

    class Meta:
        model = ServiceArea
        fields = [
            'name',
            'price',
            'polygon'
        ]
