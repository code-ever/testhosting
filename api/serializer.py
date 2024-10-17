from rest_framework import serializers
from .models import profile  # Assuming the model is named 'Profile' and not 'profile'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile  # Use the correct model class name
        fields = "__all__"  # This will include all fields in the model