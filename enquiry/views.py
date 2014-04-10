# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    ListView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .forms import EnquiryForm
from .models import Enquiry


class EnquiryCreateView(BaseMixin, CreateView):
    """Save an enquiry in the database."""

    form_class = EnquiryForm
    model = Enquiry

    def get_success_url(self):
        return reverse('project.home')


class EnquiryListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = Enquiry
