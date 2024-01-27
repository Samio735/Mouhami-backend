from django.test import SimpleTestCase
from django.urls import reverse , resolve 
from .views import booking,mybookingslawyer,lawyerapi,LawyerViewSet

class TestUrls(SimpleTestCase):
    def test_url_mybookings(self):
        url = reverse('mybookings') 
        self.assertEquals(resolve(url).func,mybookingslawyer)
        
    def test_url_lawyer_detailed(self):
        url = reverse('lawyerdetailed', args=[1]) 
        self.assertEquals(resolve(url).func,lawyerapi)
    
    def test_url_bookings(self):
        url = reverse('booking', args=[1]) 
        self.assertEquals(resolve(url).func,booking)
    
    def test_url_lawyers(self):
        url = reverse('lawyers') 
        self.assertEquals(resolve(url).func.view_class,LawyerViewSet)
    

