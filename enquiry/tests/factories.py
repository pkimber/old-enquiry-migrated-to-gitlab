# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory

from enquiry.models import Notify


class NotifyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Notify
