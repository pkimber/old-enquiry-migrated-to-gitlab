enquiry
*******

Django application for an online enquiry form.

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

Add the following to a ``.private`` file in the root of your project::

  export RECAPTCHA_PRIVATE_KEY="your private key"
  export RECAPTCHA_PUBLIC_KEY="your public key"

.. note:: Replace ``your private key`` and ``your public key`` with the actual
          reCAPTCHA keys.

Update your environment with these variables::

  source venv-enquiry/bin/activate

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_enquiry && \
      django-admin.py runserver

To login, browse to http://localhost:8000/::

  user          staff
  pass          letmein

To send email, use the ``mail_send`` management command::

  django-admin.py mail_send

Release
=======

https://www.pkimber.net/open/
