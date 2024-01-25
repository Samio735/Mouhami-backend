from rest_framework import generics, viewsets
from .models import Lawyer,Booking,Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LawyerSerializer,BookingSerializer,ReviewSerializer
class LawyerViewSet(generics.ListAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer


@api_view(['GET'])
def lawyerapi(request,id):
    if request.method =='GET' :
       
       lawyer = Lawyer.objects.get(pk=id)
       lawyer_serializer =LawyerSerializer(lawyer) 

       review = Review.objects.filter(lawyer_id=id)
       review_serializer = ReviewSerializer(review,many=True)
       return Response([lawyer_serializer.data,review_serializer.data])
    

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
    




