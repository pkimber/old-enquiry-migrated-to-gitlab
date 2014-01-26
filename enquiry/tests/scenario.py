from enquiry.tests.model_maker import make_enquiry


def default_scenario_enquiry():
    make_enquiry(
        'Rick',
        'Can I buy some hay?',
        '',
        '07840 538 357',
    )
    make_enquiry(
        'Ryan',
        (
            'Can I see some of the fencing you have done?\n'
            "I would like to see some of your standard agricultural "
            "fencing on a local dairy farm.  "
            "I like this fencing: http://en.wikipedia.org/wiki/Fencing"
        ),
        'test@pkimber.net',
        '01234 567 890',
    )
