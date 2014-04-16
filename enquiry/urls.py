# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns, url
)

from .views import EnquiryListView


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=EnquiryListView.as_view(),
        name='enquiry.list'
        ),
)
