import logging

from smtplib import SMTPException

from django.conf import settings
from django.core import mail
from django.core.management.base import BaseCommand

from django_mailgun import MailgunAPIError

from enquiry.models import (
    Enquiry,
    Notify,
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "We received an enquiry, so notify users by email."

    def _get_notify(self):
        """Return a list of emails to notify."""
        result = []
        for n in Notify.objects.all():
            result.append(n.email)
        return result

    def _send_email(self, enquiry, emails):
        """Send enquiry notification to a list of email addresses."""
        mail.send_mail(
            'Enquiry from {}'.format(enquiry.name),
            enquiry.description,
            'notify@{}'.format(settings.MAILGUN_SERVER_NAME),
            emails,
            fail_silently=False
        )

    def handle(self, *args, **options):
        emails = self._get_notify()
        enquiries = Enquiry.objects.filter(email_sent__isnull=True)
        for e in enquiries:
            try:
                self._send_email(e, emails)
            except (SMTPException, MailgunAPIError) as e:
                logger.error(e.message)
