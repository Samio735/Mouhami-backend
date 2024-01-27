from django.test import SimpleTestCase
from django.urls import reverse , resolve 
from .views import booking

class TestUrls(SimpleTestCase):
    def test_url(self):
        url = reverse('booking') 
        print(url)
        