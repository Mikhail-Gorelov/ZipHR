from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

APITestCase.maxDiff = None


class ZipAirlinesTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_create_ten_data = [
            {
                "airplane_id": 1,
                "passengers_count": 100
            },
            {
                "airplane_id": 2,
                "passengers_count": 50
            },
            {
                "airplane_id": 3,
                "passengers_count": 60
            },
            {
                "airplane_id": 4,
                "passengers_count": 70
            },
            {
                "airplane_id": 5,
                "passengers_count": 80
            },
            {
                "airplane_id": 6,
                "passengers_count": 40
            },
            {
                "airplane_id": 7,
                "passengers_count": 50
            },
            {
                "airplane_id": 8,
                "passengers_count": 50
            },
            {
                "airplane_id": 9,
                "passengers_count": 50
            },
            {
                "airplane_id": 10,
                "passengers_count": 50
            }
        ]

    def test_create_ten(self):
        url = reverse('main:zip_airlines')
        response = self.client.post(url, data=self.test_create_ten_data, format="json")
        expected_output = [
            {
                "pk": 1,
                "passengers_count": 100,
                "fuel_consumption": 0.2,
                "total_fly_minutes": 1000
            },
            {
                "pk": 2,
                "passengers_count": 50,
                "fuel_consumption": 0.6545177444479562,
                "total_fly_minutes": 611.1369835165804
            },
            {
                "pk": 3,
                "passengers_count": 60,
                "fuel_consumption": 0.9988898309344879,
                "total_fly_minutes": 600.6668417463857
            },
            {
                "pk": 4,
                "passengers_count": 70,
                "fuel_consumption": 1.2490354888959123,
                "total_fly_minutes": 640.4942110229083
            },
            {
                "pk": 5,
                "passengers_count": 80,
                "fuel_consumption": 1.4475503299472803,
                "total_fly_minutes": 690.8222666333266
            },
            {
                "pk": 6,
                "passengers_count": 40,
                "fuel_consumption": 1.513407575382444,
                "total_fly_minutes": 792.9126426480027
            },
            {
                "pk": 7,
                "passengers_count": 50,
                "fuel_consumption": 1.6567281192442507,
                "total_fly_minutes": 845.039076561722
            },
            {
                "pk": 8,
                "passengers_count": 50,
                "fuel_consumption": 1.7635532333438688,
                "total_fly_minutes": 907.2592591754342
            },
            {
                "pk": 9,
                "passengers_count": 50,
                "fuel_consumption": 1.857779661868976,
                "total_fly_minutes": 968.8985389091579
            },
            {
                "pk": 10,
                "passengers_count": 50,
                "fuel_consumption": 1.942068074395237,
                "total_fly_minutes": 1029.83001799399
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(response.json(), expected_output)
