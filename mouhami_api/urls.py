from django.urls import path

from .views import LawyerViewSet,booking,lawyerapi,mybookingslawyer,mybookingsuser,lawyerData,searchLawyer,login_view,UserRegistrationView,AvocatRegistrationView


urlpatterns = [
    path('lawyers/', LawyerViewSet.as_view()),
    path('lawyer-detailed/<int:id>', lawyerapi),
    path('lawyer-booking/<int:id>/bookings/',booking),
    path('import-lawyers/',lawyerData),
    path('mybookingsuser/',mybookingsuser),
    path('mybookingslawyer/',mybookingslawyer),
    path('search-lawyers',searchLawyer),
    path('login/',login_view),
    path('register/',UserRegistrationView.as_view()),
    path('register-lawyer/',AvocatRegistrationView.as_view()),
    
]
