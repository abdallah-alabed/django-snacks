from django.test import TestCase , SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SnacksTest(SimpleTestCase):
    def test_status_code(self):
        url1=reverse('home')
        url2=reverse('aboutus')

        res1=self.client.get(url1)
        res2=self.client.get(url2)

        self.assertEqual(res1.status_code,200)
        self.assertEqual(res2.status_code,200)


    def test_template(self):
        url1=reverse('home')
        url2=reverse('aboutus')

        res1=self.client.get(url1)
        res2=self.client.get(url2)

        self.assertTemplateUsed(res1,'home.html')
        self.assertTemplateUsed(res2,'aboutus.html')
        self.assertTemplateUsed(res1,'_parent.html')
        self.assertTemplateUsed(res2,'_parent.html')
