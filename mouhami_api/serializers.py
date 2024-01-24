from rest_framework import serializers
<<<<<<< HEAD
from .models import Lawyer,Booking,Review
=======
from .models import Lawyer,Booking 

>>>>>>> 008547b2f2393b81692bde2e18c15df630925af1

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'

<<<<<<< HEAD
class BookingSerializer(serializers.ModelSerializer):
    class Meta :
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review
=======


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
>>>>>>> 008547b2f2393b81692bde2e18c15df630925af1
        fields = '__all__'