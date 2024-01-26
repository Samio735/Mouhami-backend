from rest_framework import generics, viewsets
from .models import Lawyer,Booking,Review,Language,Specialities,User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LawyerSerializer,BookingSerializer,ReviewSerializer,LanguageSerializer,SpecialitiesSerializer,UserSerializer,UserRegistrationSerializer,LawyerRegistrationSerializer
from django.db.models import Q
import jwt
from django.conf import settings
import datetime
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




class LawyerViewSet(generics.ListAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer


@api_view(['GET'])
def lawyerapi(request,id):
    if request.method =='GET' :
       
       lawyer = Lawyer.objects.get(pk=id)
       lawyer_serializer =LawyerSerializer(lawyer) 

   
       return Response(lawyer_serializer.data)
    

@api_view(['GET','POST'])
def booking(request,id) :

    if request.method =='GET' :
       
       bookings = Booking.objects.filter(lawyer_id=id)
       booking_serializer =BookingSerializer(bookings,many=True) 
       return Response(booking_serializer.data)
    
    elif request.method == 'POST' :
       booking_serializer=BookingSerializer(data=request.data)
       if booking_serializer.is_valid():
           booking_serializer.save()
           return Response(booking_serializer.data)

@api_view(['GET'])
def mybookingslawyer(request) :
    if request.method=='GET' :
        mybookings = Booking.objects.filter(lawyer_id=1)
        mybooking_serializer =BookingSerializer(mybookings,many=True) 
        return Response(mybooking_serializer.data)


@api_view(['GET','POST'])
def mybookingsuser(request) :
    
    if request.method=='GET' :
        reviews=Review.object.all()
        review_serializer=ReviewSerializer(reviews)
        return Response(review_serializer.data)
    elif request.method == 'GET':
        # Serialize data and return response
        serializer_lawyer = LawyerSerializer(Lawyer.objects.all(), many=True)
        serializer_language = LanguageSerializer(Language.objects.all(), many=True)
        serializer_specialities = SpecialitiesSerializer(Specialities.objects.all(), many=True)
        return Response({
            "lawyers": serializer_lawyer.data,
            "languages": serializer_language.data,
            "specialities": serializer_specialities.data
        })


        mybookings = Booking.objects.filter(client_id=1)
        mybooking_serializer =BookingSerializer(mybookings,many=True) 

        review = Review.objects.filter(reviewer_id=1)
        review_serializer = ReviewSerializer(review,many=True)
        return Response([mybooking_serializer.data,review_serializer.data])
    
    
    elif request.method=='POST' :
         review_serializer=ReviewSerializer(data=request.data)
         if review_serializer.is_valid():
             review_serializer.save()
             return Response(review_serializer.data)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from mouhami_api.models import Language, Lawyer, Specialities
from .serializers import LawyerSerializer, LanguageSerializer, SpecialitiesSerializer
import json
import random

@api_view(['POST'])
def lawyerData(request):
    # Read data from cabinets.json file
    with open('cabinets.json', 'r', encoding='utf-8') as json_file:
        cabinets_data = json.load(json_file)
    all_languages=[]
    if request.method == 'POST':
        Language.objects.create(name='arabic')
        Language.objects.create(name='french')
        Language.objects.create(name='english')
        for data in cabinets_data:
            # Extract categories and assign default values if not present
            specialities_data = data.get('categories', [])
            # all_languages = [language.Name for language in Language.objects.all()]
            for language in Language.objects.all():
                all_languages.append(language)

            # Check if there are languages available  
            # Randomly select 1 or 2 languages
            num_languages_to_select = random.randint(1, min(2, len(Language.objects.all())))
            languages_data = random.sample(all_languages, num_languages_to_select)
            language_instances = []
            for lang in languages_data:
                
                language_instance= Language.objects.get(name=lang.name)
                language_instances.append(language_instance)

            # Create and save Specialities instances
            speciality_instances = []
            for speciality_name in specialities_data:
                speciality_instance, created = Specialities.objects.get_or_create(name=speciality_name)
                speciality_instances.append(speciality_instance)

            # Create and save Lawyer instance
            lawyer_data = {
                'name': f"{data.get('name', '')} {data.get('fname', '')}",
                'email': data.get('email', ''),
                'phone': data.get('phone', ''),
                'photo': data.get('avocat_image', ''),
                'location': data.get('address', ''),
                'wilaya': data.get('wilaya', ''),
                'lng': data.get('longitude', 0.0),
                'lat': data.get('latitude', 0.0),
                'rating': data.get('rating', 0.0),
            }

            lawyer_instance = Lawyer.objects.create(**lawyer_data)

            # Update many-to-many relationships
            lawyer_instance.languages.set(language_instances)
            lawyer_instance.specialities.set(speciality_instances)

        return Response({"data inserted to the database successfully!!"})


@api_view(['POST'])
def searchLawyer(request):
    if request.method == 'POST':
        name = request.data.get('name', '')
        wilaya = request.data.get('location', '')
        langue = request.data.get('langue', '')
        categorie = request.data.get('categorie', '')
        rating = request.data.get('rating', '')

        lawyer_list = Lawyer.objects.filter(
            Q(name__icontains=name) &
            Q(location__icontains=wilaya) &
            Q(specialities__name__icontains=categorie) & 
            Q(rating__icontains=rating) &
            Q(languages__name__icontains=langue)  
        ).distinct()

        serializer = LawyerSerializer(lawyer_list, many=True)
        return Response(serializer.data)




def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'is_avocat':user.is_avocat,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'username': user.username,
        'is_avocat':user.is_avocat,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')
    return refresh_token

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'message': 'client registered  successfully',
            }
        return Response(response)



class AvocatRegistrationView(CreateAPIView):
    serializer_class = LawyerRegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'message': 'client registered  successfully',
            }
        return Response(response)


@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'email and password required')

    user = User.objects.filter(email=email).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.password == password ):
        raise exceptions.AuthenticationFailed('wrong password')
    serialized_user = UserSerializer(user).data
    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)
    response.data = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': serialized_user,
    }
    return response




