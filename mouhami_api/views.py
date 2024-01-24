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



