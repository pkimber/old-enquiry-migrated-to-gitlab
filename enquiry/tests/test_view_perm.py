# -*- encoding: utf-8 -*-
import pytest

from django.core.urlresolvers import reverse

from enquiry.tests.factories import EnquiryFactory
from login.tests.fixture import perm_check


@pytest.mark.django_db
def test_list(perm_check):
    EnquiryFactory()
    EnquiryFactory()
    url = reverse('enquiry.list')
    perm_check.staff(url)
