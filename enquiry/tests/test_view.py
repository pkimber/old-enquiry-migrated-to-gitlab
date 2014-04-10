# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
import os

from django.core.urlresolvers import reverse
from django.test import TestCase

from enquiry.models import Enquiry
from enquiry.tests.scenario import default_scenario_enquiry
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    STAFF,
)


class TestView(TestCase):

    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'
        default_scenario_login()
        default_scenario_enquiry()
        staff = get_user_staff()
        self.assertTrue(
            self.client.login(username=staff.username, password=STAFF)
        )

    def tearDown(self):
        del os.environ['RECAPTCHA_TESTING']

    def test_create(self):
        response = self.client.post(
            reverse('enquiry.create'),
            dict(
                name='Richard',
                description='Do you sell hay and straw?',
                email='richard@pkimber.net',
                recaptcha_response_field='PASSED',
            )
        )
        self.assertEqual(response.status_code, 302)
        # check enquiry
        try:
            Enquiry.objects.get(name='Richard')
        except Enquiry.DoesNotExist:
            self.fail('cannot find new enquiry')

    def test_list(self):
        response = self.client.get(reverse('enquiry.list'))
        self.assertEqual(response.status_code, 200)
