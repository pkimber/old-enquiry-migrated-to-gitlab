enquiry
*******

Django application for an online enquiry.

Install
=======

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-enquiry
  source venv-enquiry/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

.. note:: Replace ``your private key`` and ``your public key`` with the actual
          reCAPTCHA keys.

::

  export RECAPTCHA_PRIVATE_KEY="your private key"
  export RECAPTCHA_PUBLIC_KEY="your public key"

::

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_enquiry && \
      django-admin.py runserver

Release
=======

https://django-dev-and-deploy-using-salt.readthedocs.org/
