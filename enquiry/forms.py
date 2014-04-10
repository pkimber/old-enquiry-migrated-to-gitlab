# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django import forms

from captcha.fields import ReCaptchaField

from base.form_utils import RequiredFieldForm

from .models import Enquiry


class EnquiryForm(RequiredFieldForm):

    """user is not logged in... so we need a captcha."""
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        for name in ('name', 'description', 'email', 'phone'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-1-2', 'rows': 4}
            )

    class Meta:
        model = Enquiry
        fields = ('name', 'description', 'email', 'phone')
