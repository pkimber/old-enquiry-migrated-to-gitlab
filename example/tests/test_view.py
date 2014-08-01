# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import TEST_PASSWORD
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
)
from mail.management.commands import mail_send

from enquiry.models import (
    Enquiry,
    Notify,
)
from enquiry.tests.scenario import default_scenario_enquiry


class TestView(TestCase):

    def _get_enquiry(self):
        return Enquiry.objects.get(name='Richard')

    def _post_enquiry(self):
        response = self.client.post(
            reverse('example.enquiry.create'),
            dict(
                name='Richard',
                description='Do you sell hay and straw?',
                email='richard@pkimber.net',
                phone='07840 538 357',
                recaptcha_response_field='PASSED',
            )
        )
        self.assertEqual(response.status_code, 302)
        return response

    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'
        default_scenario_login()
        default_scenario_enquiry()
        staff = get_user_staff()
        self.assertTrue(
            self.client.login(username=staff.username, password=TEST_PASSWORD)
        )

    def tearDown(self):
        del os.environ['RECAPTCHA_TESTING']

    def test_create(self):
        """check enquiry."""
        self._post_enquiry()
        try:
            Enquiry.objects.get(name='Richard')
        except Enquiry.DoesNotExist:
            self.fail('cannot find new enquiry')

    def test_create_no_notify(self):
        """check enquiry with no users to notify.

        Will write an error message to the log file, and won't send any
        emails.

        """
        Notify.objects.all().delete()
        self._post_enquiry()
        try:
            Enquiry.objects.get(name='Richard')
        except Enquiry.DoesNotExist:
            self.fail('cannot find new enquiry')

    def test_enquiry_email(self):
        self._post_enquiry()
        enquiry = Enquiry.objects.get(name='Richard')
        message = enquiry.message
        self.assertIn((
                'enquiry received from Richard, '
                'richard@pkimber.net on 07840 538 357'
            ),
            message.description
        )
        self.assertIn('Do you sell hay and straw?', message.description)
        self.assertIn('http://testserver/enquiry/', message.description)


    def test_send_emails(self):
        """Test the management command."""
        self._post_enquiry()
        enquiry = self._get_enquiry()
        message = enquiry.message
        count = 0
        for m in message.mail_set.all():
            self.assertIsNone(m.sent)
            count = count + 1
        self.assertEqual(2, count)
        # send the emails
        command = mail_send.Command()
        command.handle()
        # check they have been sent
        self.assertEqual(len(mail.outbox), 2)
        # check the mail is marked as sent
        message = enquiry.message
        count = 0
        for m in message.mail_set.all():
            self.assertIsNotNone(m.sent)
            count = count + 1
        self.assertEqual(2, count)
