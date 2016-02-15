# -*- encoding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models

from reversion import revisions as reversion

from base.model_utils import TimeStampedModel
from mail.models import Message


class Enquiry(TimeStampedModel):

    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return '{}: {}, {}'.format(
            self.name,
            self.email,
            self.phone,
        )

    def clean(self):
        if self.phone or self.email:
            pass
        else:
            raise ValidationError(
                'You must provide an email address or phone number.'
            )

    @property
    def message(self):
        """Get the mail message linked to this enquiry."""
        return Message.objects.get(
            object_id=self.pk,
            content_type=ContentType.objects.get_for_model(self),
        )

reversion.register(Enquiry)
