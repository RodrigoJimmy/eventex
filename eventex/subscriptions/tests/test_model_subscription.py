from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Rodrigo Vieira',
            cpf='12345678901',
            email='rodrigo@vieira.net',
            phone='45-998275857',
        )
        self.obj.save()
    
    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Rodrigo Vieira', str(self.obj))
