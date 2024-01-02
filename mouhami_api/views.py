from rest_framework import generics, viewsets
from .models import Lawyer
from .serializers import LawyerSerializer
class LawyerViewSet(generics.ListAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer
# added some views here 