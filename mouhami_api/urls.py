from django.urls import path

from .views import LawyerViewSet,booking,lawyerapi,mybookingslawyer,mybookingsuser,lawyerData,searchLawyer,login_view,UserRegistrationView,AvocatRegistrationView,UserViewSet


urlpatterns = [
    path('lawyers/', LawyerViewSet.as_view(),name='lawyers'),
    path('lawyer-detailed/<int:id>', lawyerapi , name='lawyerdetailed'),
    path('lawyer-booking/<int:id>/bookings/',booking, name='booking'),
    path('import-lawyers/',lawyerData),
    path('mybookingsuser/',mybookingsuser,name='mybookingsuser'),
    path('mybookingslawyer/',mybookingslawyer, name='mybookings'),
    path('search-lawyers',searchLawyer),
    path('login/',login_view),
    path('register/',UserRegistrationView.as_view()),
    path('register-lawyer/',AvocatRegistrationView.as_view()),
    path('users/',UserViewSet.as_view()),
    
]
