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

  python setup.py install


Running Migrations
------------------

  eukalypse_now init
  python manage.py syncdb
  python manage.py migrate





Starting the Web Service
------------------------


  eukalypse_now  run_gunicorn 0.0.0.0:8000 -w 3
