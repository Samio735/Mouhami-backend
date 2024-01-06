from rest_framework import serializers
from .models import Lawyer,Language,Specialities

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'



class SpecialitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialities
        fields = '__all__'

