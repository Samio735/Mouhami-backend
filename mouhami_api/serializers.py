from rest_framework import serializers
from .models import Lawyer,Booking,Review,Language,Specialities

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'
    # get related reviews
    reviews = serializers.SerializerMethodField()
    def get_reviews(self, obj):
        reviews = Review.objects.filter(lawyer_id=obj.id)
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

class BookingSerializer(serializers.ModelSerializer):
    class Meta :
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review
        fields = '__all__'
        depth = 1







class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'



class SpecialitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialities
        fields = '__all__'

