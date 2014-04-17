# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.tests.model_maker import clean_and_save

from enquiry.models import (
    Enquiry,
    Notify,
)


def make_enquiry(name, description, email, phone, **kwargs):
    defaults = dict(
        name=name,
        description=description,
        phone=phone,
        email=email,
    )
    defaults.update(kwargs)
    return clean_and_save(Enquiry(**defaults))


def make_notify(email, **kwargs):
    defaults = dict(
        email=email,
    )
    defaults.update(kwargs)
    return clean_and_save(Notify(**defaults))
