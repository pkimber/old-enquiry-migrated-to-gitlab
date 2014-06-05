# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from captcha.fields import ReCaptchaField

from base.form_utils import RequiredFieldForm
from mail.service import queue_mail_message

from .models import (
    Enquiry,
    Notify,
)


class EnquiryForm(RequiredFieldForm):

    """user is not logged in... so we need a captcha."""
    captcha = ReCaptchaField(attrs={'theme': 'white'})

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        for name in ('name', 'description', 'email', 'phone'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-1-2', 'rows': 4}
            )

    class Meta:
        model = Enquiry
        fields = ('name', 'description', 'email', 'phone')

    def save(self, commit=True):
        instance = super(EnquiryForm, self).save(commit)
        if commit:
            email_addresses = [n.email for n in Notify.objects.all()]
            queue_mail_message(
                instance,
                email_addresses,
                'Enquiry from {}'.format(instance.name),
                instance.description,
            )
        return instance
