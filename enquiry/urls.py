from django.conf.urls import (
    patterns, url
)

from .views import (
    EnquiryCreateView,
    EnquiryListView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^add/$',
        view=EnquiryCreateView.as_view(),
        name='enquiry.create'
        ),
    url(regex=r'^$',
        view=EnquiryListView.as_view(),
        name='enquiry.list'
        ),
)
