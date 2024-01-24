from rest_framework import generics, viewsets
from .models import Lawyer,Booking,Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LawyerSerializer,BookingSerializer,ReviewSerializer
class LawyerViewSet(generics.ListAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer
<<<<<<< HEAD
@api_view(['GET'])
def lawyerapi(request,id):
    if request.method =='GET' :
       
       lawyer = Lawyer.objects.get(pk=id)
       lawyer_serializer =LawyerSerializer(lawyer) 
       return Response(lawyer_serializer.data)
    

@api_view(['GET','POST'])
def booking(request,lawyer_id) :

    if request.method =='GET' :
       
       bookings = Booking.objects.filter(pk=lawyer_id)
       booking_serializer =BookingSerializer(bookings,many=True) 
       return Response(booking_serializer.data)
    
    elif request.method == 'POST' :
       booking_serializer=BookingSerializer(data=request.data)
       if booking_serializer.is_valid():
           booking_serializer.save()
           return Response("Added successfully")
       

def reviews(request) :
    if request.method=='GET' :
        reviews=Review.object.all()
        review_serializer=ReviewSerializer(reviews)
        return Response(review_serializer.data)
=======
# added some views here 
>>>>>>> 008547b2f2393b81692bde2e18c15df630925af1
