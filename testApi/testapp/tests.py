from django.test import TestCase
from django.urls import reverse
from . models import info

# Create your tests here.
class ViewTests(TestCase):

    def setUp(self):
        testdata = info.objects.create(lastcommitsha='test', version='0.1', description='testingapp')
        testdata.save()

    def test_msg_is_hello(self):
        resp = self.client.get(reverse('hello'))
        self.assertContains(resp, 'Hello, world')

    def test_info_status(self):
        resp = self.client.get(reverse('info'))
        self.assertEqual(resp.status_code, 200)

    def test_404_status(self):
        resp = self.client.get('/test/')
        self.assertEqual(resp.status_code, 404)
