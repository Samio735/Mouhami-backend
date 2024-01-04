from rest_framework import serializers
from .models import Lawyer,Booking 


class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'