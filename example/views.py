# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    TemplateView,
)

from base.view_utils import BaseMixin
from enquiry.forms import EnquiryForm
from enquiry.models import Enquiry


class HomeView(TemplateView):

    template_name = 'example/home.html'


class EnquiryCreateView(BaseMixin, CreateView):
    """Save an enquiry in the database."""

    form_class = EnquiryForm
    model = Enquiry

    def get_form_kwargs(self):
        kwargs = super(EnquiryCreateView, self).get_form_kwargs()
        kwargs.update(dict(
            request=self.request,
            user=self.request.user,
        ))
        return kwargs

    def get_success_url(self):
        return reverse('project.home')
