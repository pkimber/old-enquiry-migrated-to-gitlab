# -*- encoding: utf-8 -*-
import factory

from enquiry.models import Enquiry


class EnquiryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Enquiry
