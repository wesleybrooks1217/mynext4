from django.test import TestCase

from .models import College

# Create your tests here.

class CollegeTestCase(TestCase):
    def setUp(self):
        College.objects.create(
            name='Brown University',
            city='Providence, RI',
            public=False,
            year_est=1764,
            description='Some lengthy boring description'
        )

    def test_college_data(self):
        c = College.objects.get(name='Brown University')
        self.assertEqual(str(c), 'Brown University')
        self.assertEqual(c.years_since_est(), 2022 - 1764)
