from django.test import TestCase
from .models import Publisher


class TestPublisherModel(TestCase):
    """Test the Publisher model"""
    def setUp(self):
        self.p = Publisher(name="Packt",
                           website='www.packt.com',
                           email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsNotNone(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")

