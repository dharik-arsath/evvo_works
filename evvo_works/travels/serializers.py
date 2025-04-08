from rest_framework import serializers
from .models import TravelRequest

class TravelRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelRequest
        fields = ['id', 'destination', 'purpose', 'start_date', 'end_date', 'status', 'created_at']
        read_only_fields = ['id','created_at', 'status']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return TravelRequest.objects.create(**validated_data)

class TravelRequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelRequest
        fields = ['status']

    def validate_status(self, value):
        if value not in ['approved', 'rejected']:
            raise serializers.ValidationError("Invalid status, Must be either 'approved' or 'rejected'")
        return value