from rest_framework import serializers
from .models import Doctors

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"