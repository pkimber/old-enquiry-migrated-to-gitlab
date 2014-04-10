# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.core import mail
from django.test import TestCase

from enquiry.management.commands import (
    demo_data_enquiry,
    enquiry_send_emails,
    init_app_enquiry,
)
from enquiry.tests.scenario import (
    default_scenario_enquiry,
    get_enquiry_buy_some_hay,
)
from login.management.commands import demo_data_login
from login.tests.scenario import default_scenario_login


class TestCommand(TestCase):

    def test_demo_data(self):
        """Test the management command."""
        pre_command = demo_data_login.Command()
        pre_command.handle()
        command = demo_data_enquiry.Command()
        command.handle()

    def test_init_app(self):
        """Test the management command."""
        command = init_app_enquiry.Command()
        command.handle()

    def test_send_emails(self):
        """Test the management command."""
        default_scenario_login()
        default_scenario_enquiry()
        self.assertIsNone(get_enquiry_buy_some_hay().email_sent)
        command = enquiry_send_emails.Command()
        command.handle()
        self.assertEqual(len(mail.outbox), 1)
        self.assertIsNotNone(get_enquiry_buy_some_hay().email_sent)
