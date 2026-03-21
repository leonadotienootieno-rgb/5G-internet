from django.test import TestCase, Client


class LandingViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_landing_get_renders(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Check Airtel 5G Availability')

    def test_thankyou_view_renders(self):
        response = self.client.get('/thank-you/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank You')

