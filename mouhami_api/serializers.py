from rest_framework import serializers
from .models import Lawyer,Booking,Review

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta :
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review
        fields = '__all__'