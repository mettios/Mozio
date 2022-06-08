from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'name',
            'email',
            'language',
            'phone',
            'currency'
        ]
# can define a new variable that doesnt really exist but is based
# on one of the fields
