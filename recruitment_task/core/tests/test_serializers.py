from django.test import TestCase

from core.serializers import ProjectDetailsSerializer, InvestorDetailsSerializer


class ProjectDetailsSerializerTestCase(TestCase):
    "Test case for ProjectDetailSerializer related to Project Model."

    def setUp(self) -> None:
        self.data = {
            "name": "test",
            "description": "test",
            "amount": "500.00",
            "delivery_date": "2022-01-21",
        }

    def test_deserialize_project_data(self):
        """Deserialize data with ProjectDetailSerializer"""
        serializer = ProjectDetailsSerializer(data=self.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print('--Error::', serializer.errors) # This is for debugging.
        self.assertEqual(serializer.data['name'], 'test')
        self.assertEqual(serializer.data['description'], 'test')
        self.assertEqual(serializer.data['amount'], '500.00')
        self.assertEqual(serializer.data['delivery_date'], '2022-01-21')


class InvestorDetailsSerializerTestCase(TestCase):
    "Test case for InvestorDetailSerializer related to Investor Model."
    def setUp(self) -> None:
        self.data = {
            "name": "Test Investor",
            "remaining_amount": "9000.00",
            "total_amount": "8000",
            "individual_amount": "7000.00",
            "project_delivery_deadline": "2022-02-01"
        }

    def test_deserialize_investor_data(self):
        """Deserialize data with InvestorDetailsSerializer"""
        serializer = InvestorDetailsSerializer(data=self.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print('--Error::', serializer.errors) # This is for debugging.
        self.assertEqual(serializer.data["name"], "Test Investor")
        # This will be actually '8000.00' not '9000.00' because of signal used.
        self.assertEqual(serializer.data['remaining_amount'], '8000.00')
        self.assertEqual(serializer.data['total_amount'], '8000.00')
        self.assertEqual(serializer.data['individual_amount'], "7000.00")
        self.assertEqual(serializer.data['project_delivery_deadline'], '2022-02-01')