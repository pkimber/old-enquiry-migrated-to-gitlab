# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import TEST_PASSWORD
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
)

from enquiry.tests.scenario import default_scenario_enquiry


class TestView(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_enquiry()
        staff = get_user_staff()
        self.assertTrue(
            self.client.login(username=staff.username, password=TEST_PASSWORD)
        )

    def test_list(self):
        response = self.client.get(reverse('enquiry.list'))
        self.assertEqual(response.status_code, 200)
