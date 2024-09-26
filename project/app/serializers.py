from rest_framework import serializers
from .models import get_information, send_information

# Serializer for get_information
class GetInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_information
        fields = ["get_value"]

# Serializer for send_information
class SendInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = send_information
        fields = ["send_value"]
