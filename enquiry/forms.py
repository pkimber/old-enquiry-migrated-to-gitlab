from django import forms

from captcha.fields import CaptchaField

from base.form_utils import RequiredFieldForm

from .models import Enquiry


class EnquiryForm(RequiredFieldForm):
    """user is not logged in... so we need a captcha."""
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        for name in ('name', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )
        for name in ('email', 'phone'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-1-2'}
            )

    class Meta:
        model = Enquiry
        fields = ('name', 'description', 'email', 'phone')
