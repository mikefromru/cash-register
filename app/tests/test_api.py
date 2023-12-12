from django.test import TestCase
from ..models import Item
from rest_framework.test import APITestCase
from django.urls import reverse

import logging


logger = logging.getLogger(__name__)

class TestAppAPI(APITestCase):

    def test_url_on_method_get(self):
        logger.debug('Starting test url access')
        response = self.client.get(reverse('cash-machine'))
        self.assertEquals(response.status_code, 405)

    def test_url_on_method_post(self):
        payload = {'items': [1, 2, 3]}
        response = self.client.post(reverse('cash-machine'), data=payload, format='json')
        self.assertEquals(response.status_code, 200)
