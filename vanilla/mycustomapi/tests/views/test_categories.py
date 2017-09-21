from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CategoryViewTests(APITestCase):
    fixtures = ['catalogue.json']
    """
    def test_get_category_list(self):
        url = reverse('category-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')
    """
    
    def test_get_category_list(self):
        url = reverse('category-list')
        response = self.client.get(url, format='json')
        print('response', response, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

