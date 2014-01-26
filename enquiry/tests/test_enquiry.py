from django.core.exceptions import ValidationError
from django.test import TestCase

from enquiry.models import Enquiry
from enquiry.tests.model_maker import make_enquiry


class TestEnquiry(TestCase):

    def test_enquiry(self):
        """A simple enquiry."""
        make_enquiry(
            'Rachel',
            'Can I buy some hay?',
            'web@pkimber.net',
            '07840 538 357',
        )

    def test_enquiry_no_contact(self):
        """This enquiry has no contact details."""
        self.assertRaises(
            ValidationError,
            make_enquiry,
            'Ruth',
            'Can I buy some straw?',
            '',
            '',
        )

    def test_enquiry_no_description(self):
        """This enquiry has no description."""
        self.assertRaises(
            ValidationError,
            make_enquiry,
            'Ruth',
            '',
            'web@pkimber.net',
            '07840 538 357',
        )
