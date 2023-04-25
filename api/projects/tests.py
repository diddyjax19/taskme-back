from django.test import TestCase

# Create your tests here.
from .models import Project

def setUp(self):
    
        # Create Projects.
        a1 = Project.objects.create(code="AAA", city="City A")
        a2 = Project.objects.create(code="BBB", city="City B")

        
        
def test_departures_count(self):
    a = Project.objects.get(code="AAA")
    self.assertEqual(a.departures.count(), 3)

def test_arrivals_count(self):
    a = Project.objects.get(code="AAA")
    self.assertEqual(a.arrivals.count(), 1)