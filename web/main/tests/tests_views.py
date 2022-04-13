from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ZipAirlinesTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_create_ten_data = [
            {"airplane_id": 1, "passengers_count": 100},
            {"airplane_id": 2, "passengers_count": 50},
            {"airplane_id": 3, "passengers_count": 60},
            {"airplane_id": 4, "passengers_count": 70},
            {"airplane_id": 5, "passengers_count": 80},
            {"airplane_id": 6, "passengers_count": 40},
            {"airplane_id": 7, "passengers_count": 50},
            {"airplane_id": 8, "passengers_count": 50},
            {"airplane_id": 9, "passengers_count": 50},
            {"airplane_id": 10, "passengers_count": 50},
        ]
        cls.test_create_five_data = [
            {"airplane_id": 100, "passengers_count": 100},
            {"airplane_id": 200, "passengers_count": 50},
            {"airplane_id": 300, "passengers_count": 60},
            {"airplane_id": 400, "passengers_count": 70},
            {"airplane_id": 500, "passengers_count": 80},
        ]
        cls.test_create_three_data = [
            {"airplane_id": 1, "passengers_count": 400},
            {"airplane_id": 2, "passengers_count": 500},
            {"airplane_id": 3, "passengers_count": 600},
        ]

    def test_create_ten(self):
        url = reverse('main:zip_airlines')
        response = self.client.post(url, data=self.test_create_ten_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 10)

    def test_create_five(self):
        url = reverse('main:zip_airlines')
        response = self.client.post(url, data=self.test_create_five_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 5)

    def test_create_three(self):
        url = reverse('main:zip_airlines')
        response = self.client.post(url, data=self.test_create_three_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 3)
