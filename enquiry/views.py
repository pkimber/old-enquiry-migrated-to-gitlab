# -*- encoding: utf-8 -*-
from django.views.generic import ListView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .models import Enquiry


class EnquiryCreateMixin:

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(dict(
            request=self.request,
            user=self.request.user,
        ))
        return kwargs


class EnquiryListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    paginate_by = 10
    model = Enquiry
