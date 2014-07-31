# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .factories import NotifyFactory


class TestNotify(TestCase):

    def test_str(self):
        notify = NotifyFactory(email='test@pkimber.net')
        self.assertEquals(str(notify), 'test@pkimber.net')
