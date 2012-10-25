Quickstart
==========

Some basic prerequisites which you'll need in order to run eukalypse_now:

* Python 2.7
* python-setuptools, python-dev
* Ideally a real database (like PostgreSQL or MySQL)
* Likely a UNIX-based operating system

This guide will step you through setting up a virtualenv, installing the required packages,
and configuring the basic web service.

Setting up an Environment
-------------------------

The first thing you'll need is the Python ``virtualenv`` package. You probably already
have this, but if not, you can install it with::

  easy_install -U virtualenv

Once that's done, choose a location for the environment, and create it with the ``virtualenv``
command. For our guide, we're going to choose ``/www/eukalypse_now/``::

  virtualenv /www/eukalypse_now/

Finally, activate your virtualenv::

  source /www/eukalypse_now/bin/activate

.. note:: Activating the environment adjusts your PATH, so that things like easy_install now
          install into the virtualenv by default.




Install eukalypse_now
--------------

Once you've got the environment setup, you can install eukalypse_now and all its dependencies::

  python pip install -r requirements.txt


Running Migrations
------------------

  python manage.py syncdb
  python manage.py migrate



Configure Outbound Mail
-----------------------

Several settings exist as part of the Django framework which will configure your outbound mail server. For the
standard implementation, using a simple SMTP server, you can simply configure the following::

    EMAIL_HOST = 'localhost'
    EMAIL_HOST_PASSWORD = ''
    EMAIL_HOST_USER = ''
    EMAIL_PORT = 25
    EMAIL_USE_TLS = False

Being that Django is a pluggable framework, you also have the ability to specify different mail backends. See the `official Django documentation <https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#email-backends>`_ for more information on alterantive backends.


Starting the Web Service
------------------------


  python manage.py runserver
