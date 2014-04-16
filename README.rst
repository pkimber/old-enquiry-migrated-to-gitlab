ENQUIRY
*******

Django application for an online enquiry.

Install
=======

Virtual Environment
-------------------

.. note:: Replace ``patrick`` with your name (check in the ``settings`` folder
          to make sure a file has been created for you).

.. note:: Replace ``your private key`` and ``your public key`` with the actual
          reCAPTCHA keys.

  mkvirtualenv dev_enquiry
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=example.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

  echo "export RECAPTCHA_PRIVATE_KEY=\"your private key\"" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset RECAPTCHA_PRIVATE_KEY" >> $VIRTUAL_ENV/bin/postdeactivate

  echo "export RECAPTCHA_PUBLIC_KEY=\"your public key\"" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset RECAPTCHA_PUBLIC_KEY" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv .
  deactivate

Testing
=======

Using ``pytest-django``::

  workon dev_enquiry
  find . -name '*.pyc' -delete
  py.test

To stop on first failure::

  py.test -x

Usage
=====

::

  workon dev_enquiry

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_enquiry && \
      django-admin.py runserver

Release
=======

https://github.com/pkimber/docs
