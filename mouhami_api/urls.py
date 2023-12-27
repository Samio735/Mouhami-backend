from django.urls import path
from .views import LawyerViewSet

urlpatterns = [
    path('lawyers/', LawyerViewSet.as_view()),
]
