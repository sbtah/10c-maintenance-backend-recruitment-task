from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.utils import timezone

from core.models import Investor, Project


class InvestorDetailsViewTestCase(TestCase):
    @staticmethod
    def _get_url(investor_id):
        return f'/investors/{investor_id}/'

    def setUp(self) -> None:
        self.investor = Investor.objects.create(
            name='test_name', total_amount=100000, individual_amount=500,
            project_delivery_deadline=timezone.now() + timezone.timedelta(days=21)
        )
        self.client = APIClient()

    def test_get(self):
        url = self._get_url(self.investor.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        investor_data = response.data

        self.assertEqual(investor_data['id'], self.investor.id)
        self.assertEqual(investor_data['name'], self.investor.name)


class ProjectDetailsViewTestCase(TestCase):
    @staticmethod
    def _get_url(investor_id):
        return f'/projects/{investor_id}/'

    def setUp(self) -> None:
        self.project = Project.objects.create(
            name='test_name', description='test', amount=500,
            delivery_date=timezone.now() + timezone.timedelta(days=21)
        )
        self.client = APIClient()

    def test_get(self):
        url = self._get_url(self.project.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project_data = response.data

        self.assertEqual(project_data['id'], self.project.id)
        self.assertEqual(project_data['name'], self.project.name)


class MatchingProjectsViewTest(TestCase):
    """Testcase for MatchingProjectsView."""

    @staticmethod
    def _get_url(investor_id):
        return f'/investors/{investor_id}/matches/'
    
    def setUp(self):
        self.investor = Investor.objects.create(
            name='INVESTOR 1',
            remaining_amount=50000.00,
            total_amount=100000.00,
            individual_amount=5000.00,
            project_delivery_deadline='2022-02-22',
        )
        self.project_1 = Project.objects.create(
            name='PROJECT 1',
            description='test_1',
            amount=500.00,
            delivery_date='2022-01-22',
        )
        self.project_2 = Project.objects.create(
            name='PROJECT 2',
            description='test_2',
            amount=11000.00,
            delivery_date='2024-01-22',
        )
    
        self.client = APIClient()

    def test_matching_projects_list(self):
        """Test that proper projects are listed."""
        url = self._get_url(self.investor.id)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], 'PROJECT 1')


class MathingInvestorsViewTest(TestCase):
    """Testcase for MathingInvestorsView."""

    @staticmethod
    def _get_url(product_id):
        return f'/projects/{product_id}/matches/'
    
    def setUp(self):

        self.project_1 = Project.objects.create(
            name='PROJECT 1',
            description='test_1',
            amount=500.00,
            delivery_date='2023-01-22',
        )
        self.investor_1 = Investor.objects.create(
            name='INVESTOR 1',
            remaining_amount=50000.00,
            total_amount=100000.00,
            individual_amount=500.00,
            project_delivery_deadline='2022-02-22',
        )

        self.investor_2 = Investor.objects.create(
            name='INVESTOR 2',
            remaining_amount=50000.00,
            total_amount=100000.00,
            individual_amount=500.00,
            project_delivery_deadline='2024-02-22',
        )

        self.client = APIClient()

    def test_matching_investors_list(self):
        """Test that proper projects are listed."""
        url = self._get_url(self.project_1.id)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)