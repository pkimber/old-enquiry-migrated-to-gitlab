from base.tests.model_maker import clean_and_save

from enquiry.models import Enquiry


def make_enquiry(name, email, phone, **kwargs):
    defaults = dict(
        name=name,
        phone=phone,
        email=email,
    )
    defaults.update(kwargs)
    return clean_and_save(Enquiry(**defaults))
