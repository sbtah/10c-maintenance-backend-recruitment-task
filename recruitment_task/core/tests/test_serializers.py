from django.test import TestCase

from core.serializers import ProjectDetailsSerializer


class ProjectDetailsSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            "name": "test",
            "description": "test",
            "amount": "500.00",
            "delivery_date": "2022-01-21"
        }

    def test_deserialize(self):
        serializer = ProjectDetailsSerializer(data=self.data)
        serializer.is_valid()
        instance = serializer.save()
