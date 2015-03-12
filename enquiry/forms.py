# -*- encoding: utf-8 -*-
import logging

from django.core.urlresolvers import reverse

from nocaptcha_recaptcha.fields import NoReCaptchaField

from base.form_utils import RequiredFieldForm
from mail.models import Notify
from mail.service import queue_mail_message
from mail.tasks import process_mail

from .models import Enquiry


logger = logging.getLogger(__name__)


class EnquiryForm(RequiredFieldForm):

    """user is not logged in... so we need a captcha."""
    captcha = NoReCaptchaField()

    def __init__(self, *args, **kwargs):
        """Don't use the captcha if the user is already logged in."""
        user = kwargs.pop('user')
        self.req = kwargs.pop('request')
        super(EnquiryForm, self).__init__(*args, **kwargs)
        if user.is_authenticated():
            del self.fields['captcha']
        for name in ('name', 'description', 'email', 'phone'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-1-2', 'rows': 4}
            )

    class Meta:
        model = Enquiry
        fields = ('name', 'description', 'email', 'phone')

    def _email_message(self, enquiry):
        result = '{} - enquiry received from {}, '.format(
            enquiry.created.strftime('%d/%m/%Y %H:%M'),
            enquiry.name,
        )
        if enquiry.email:
            result = result + '{} '.format(enquiry.email)
        if enquiry.phone:
            result = result + 'on {}'.format(enquiry.phone)
        result = result + ':\n\n{}\n\n{}'.format(
            enquiry.description,
            self.req.build_absolute_uri(reverse('enquiry.list')),
        )
        return result

    def save(self, commit=True):
        instance = super(EnquiryForm, self).save(commit)
        if commit:
            email_addresses = [n.email for n in Notify.objects.all()]
            if email_addresses:
                queue_mail_message(
                    instance,
                    email_addresses,
                    'Enquiry from {}'.format(instance.name),
                    self._email_message(instance),
                )
                process_mail.delay()
            else:
                logging.error(
                    "Enquiry app cannot send email notifications.  "
                    "No email addresses set-up in 'enquiry.models.Notify'"
                )
        return instance
