from rest_framework import generics, viewsets
from .models import Lawyer,Booking,Review
from mouhami_api.models import Language, Lawyer, Specialities
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import random
from .serializers import LawyerSerializer,BookingSerializer,ReviewSerializer,LanguageSerializer, SpecialitiesSerializer

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



@api_view(['POST'])
def lawyerData(request):
    with open('cabinets.json', 'r', encoding='utf-8') as json_file:
        cabinets_data = json.load(json_file)
    all_languages=[]
    if request.method == 'POST':
        Language.objects.create(name='arabic')
        Language.objects.create(name='french')
        Language.objects.create(name='english')
        for data in cabinets_data:
            specialities_data = data.get('categories', [])
            for language in Language.objects.all():
                all_languages.append(language)

            num_languages_to_select = random.randint(1, min(2, len(Language.objects.all())))
            languages_data = random.sample(all_languages, num_languages_to_select)
            language_instances = []
            for lang in languages_data:
                
                language_instance= Language.objects.get(name=lang.name)
                language_instances.append(language_instance)

            speciality_instances = []
            for speciality_name in specialities_data:
                speciality_instance, created = Specialities.objects.get_or_create(name=speciality_name)
                speciality_instances.append(speciality_instance)

            lawyer_data = {
                'name': f"{data.get('name', '')} {data.get('fname', '')}",
                'email': data.get('email', ''),
                'phone': data.get('phone', ''),
                'photo': data.get('avocat_image', ''),
                'location': data.get('address', ''),
                'lng': data.get('longitude', 0.0),
                'lat': data.get('latitude', 0.0),
                'rating': data.get('rating', 0.0),
            }

            lawyer_instance = Lawyer.objects.create(**lawyer_data)

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



