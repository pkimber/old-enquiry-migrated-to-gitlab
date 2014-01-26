from enquiry.tests.model_maker import make_enquiry


def default_scenario_enquiry():
    make_enquiry(
        'Can I buy some hay?',
        'web@pkimber.net',
        '07840 538 357',
    )
    make_enquiry(
        'Can I see some of the fencing you have done?',
        'test@pkimber.net',
        '01234 567 890',
    )
