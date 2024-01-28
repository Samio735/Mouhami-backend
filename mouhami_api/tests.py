from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse , resolve 
from .views import booking,mybookingslawyer,lawyerapi,LawyerViewSet
from .models import Review,Booking,Lawyer,User
import json


#testing urls
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
    
#testing views
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.lawyers_list = reverse('lawyers')
        self.test_lawyer = Lawyer.objects.create(name='TestLawyer',phone='0556044235',email='test@gmail.com')
        self.lawyer_detailed = reverse('lawyerdetailed',args=[self.test_lawyer.id])
        self.mybookingsuser=reverse('mybookingsuser')
        self.booking_url=reverse('booking',args=[self.test_lawyer.id])
        self.test_user=User.objects.create_user(username='test',password='test')
       


    def test_lawyers_list_GET(self):
        
        response=self.client.get(self.lawyers_list)
        self.assertEquals(response.status_code,200)
    
    def test_lawyer_detailed_GET(self):
        
        response=self.client.get(self.lawyer_detailed)
        self.assertEquals(response.status_code,200)

    def test_mybookingsuser_GET(self):
        response = self.client.get(self.mybookingsuser)
        self.assertEquals(response.status_code,200)

    def test_add_booking_POST(self):
        data={
             "date": "2025-01-27",
    "time": 2104,
    "lawyer_id": self.test_lawyer.id,
    "client_id": self.test_user.id,
           }
       
        response=self.client.post(self.booking_url,data,format='json')
        
        self.assertEquals(response.status_code,200)
        book =Booking.objects.get(lawyer_id=self.test_lawyer.id)
        
        self.assertEquals(book.time,2104)

    
    def test_add_booking_POST_no_data(self):
        data={}

        response=self.client.post(self.booking_url,data,format='json')
        
        self.assertEquals(response.status_code,400)
    
    