from django.test import TestCase
from core.businesslogic.investing import invest_into_project
from core.models import Investor, Project
from core.businesslogic.errors import CannotInvestIntoProjectException


class MatchmakingTestCase(TestCase):
    """Test case for Matchmaking business logic."""

    def setUp(self):
        self.investor_1 = Investor.objects.create(
            name='INVESTOR 1',
            remaining_amount=50000.00,
            total_amount=100000.00,
            individual_amount=5000.00,
            project_delivery_deadline='2022-02-22',
        )
        self.investor_2 = Investor.objects.create(
            name='INVESTOR 2',
            remaining_amount=999.00,
            total_amount=999.00,
            individual_amount=222.00,
            project_delivery_deadline='2021-12-22',
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

    def test_matchmaking_logic(self):
        """Test investing into wrong projects raises Exeption."""
        self.assertRaises(CannotInvestIntoProjectException, invest_into_project, self.investor_1, self.project_2,)
        self.assertRaises(CannotInvestIntoProjectException, invest_into_project, self.investor_2, self.project_1,)
