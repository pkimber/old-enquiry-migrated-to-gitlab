enquiry
*******

Django application for an online enquiry form.

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-enquiry
  source venv-enquiry/bin/activate
  pip install --upgrade pip

  pip install -r requirements/local.txt

Add the following to a ``.private`` file in the root of your project::

  export NORECAPTCHA_SITE_KEY="<your site key>"
  export NORECAPTCHA_SECRET_KEY="<your secret key>"

.. note:: Replace ``<your site key>`` and ``<your secret key>`` with the
          actual reCAPTCHA keys.

.. warning:: The ``.private`` file should not be added to a public repository,
             as it contains *secret* information.  So please do not add it to
             ``git`` or ``mercurial``.

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

  ./init_dev.sh

To login, browse to http://localhost:8000/::

  user          staff
  pass          letmein

To send email, use the ``mail_send`` management command::

  django-admin.py mail_send

Release
=======

https://www.kbsoftware.co.uk/docs/
