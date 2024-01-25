from django.urls import path

from .views import LawyerViewSet,booking,lawyerapi,mybookingslawyer,mybookingsuser,lawyerData


urlpatterns = [
    path('lawyers/', LawyerViewSet.as_view()),
    path('lawyer-detailed/<int:id>', lawyerapi),
    path('lawyer-booking/<int:id>/bookings/',booking),
    path('import-lawyers/',lawyerData),
    path('mybookingsuser/',mybookingsuser),
    path('mybookingslawyer/',mybookingslawyer),
    path('search-lawyers',searchLawyer),
]
