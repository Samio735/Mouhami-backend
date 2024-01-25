from rest_framework import serializers
from .models import Lawyer,Booking,Review,Language,Specialities,User

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




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','first_name','last_name','is_avocat')




class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'



class SpecialitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialities
        fields = '__all__'


class LawyerRegistrationSerializer(serializers.ModelSerializer):  
    password1 = serializers.CharField(write_only=True, required=True,)
    password2 = serializers.CharField(write_only=True, required=True)
    Avocat_data = LawyerSerializer(required=False)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2','Avocat_data')
        extra_kwargs = {'password1': {'write_only': True}}
    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        username = validated_data.pop('username')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email= validated_data.pop('email')
        password = validated_data.pop('password1')
        profile_data = validated_data.pop('Avocat_data')
        user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_avocat=True,auth_provider='gmail',is_active=False)
        user.save()
        Av=Lawyer.objects.create(
            user=user,
            location=profile_data['address'],
            phone=profile_data['phone'],
            specialities=profile_data['specialities'],
            languages=profile_data['languages'],
            wilaya=profile_data['wilaya'],
            photo=profile_data['avocat_image'],
            lat=profile_data['lat'],
            lng=profile_data['lng'],            
        )
        return Av
    
    
class UserRegistrationSerializer(serializers.ModelSerializer):  
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2')
        extra_kwargs = {'password1': {'write_only': True}}
    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        username = validated_data.pop('username')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email= validated_data.pop('email')
        password = validated_data.pop('password1')
        user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_client=True,is_active=True,auth_provider='gmail')
        user.save()
        return user

