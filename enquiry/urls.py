# -*- encoding: utf-8 -*-
from django.conf.urls import url

from .views import EnquiryListView

urlpatterns = [
    url(regex=r'^$',
        view=EnquiryListView.as_view(),
        name='enquiry.list'
        ),
]
