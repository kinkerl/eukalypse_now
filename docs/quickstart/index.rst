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

Get the code
----------------------

It is available through pip but due to a bug in celery/billiard/logan, it is not the recommended way to install euakalypse_now.
First you have to get the code from github.::

  git clone git://github.com/kinkerl/eukalypse_now.git && cd eukalypse_now

          
          
Install eukalypse_now
----------------------

Check if you are still inside your new virtual environment. If you are, you can install eukalypse_now and all its dependencies::

  python setup.py install


Settings
--------

Create a custom settings file in ~/.eukalypse_now/ ::

  eukalypse_now init

Check the configuration in ~/.eukalypse_now//eukalypse_now.conf.py and update it to your needs.

Database setup / Migrations
----------------------------

eukalypse_now needs a database to store the tests and testresults.
Create a database in ~/.eukalypse_now/::

  eukalypse_now syncdb
  eukalypse_now migrate

Start the Server
----------------

eukalypse_now needs 2 servers to function, celery and the admin interface. 
You have to start both and both inside your virtual environment.


Starging Celery
________________

This daemon is for running checks at night.

.. warning:: This optimal way is broken right now due to a bug in logan or billiard: https://github.com/dcramer/logan/issues/7 it should be 'eukalypse_now celeryd -E -B -I eukalypse_now.tasks' ... now to the workaround:

You have to change in source directory, get the config and run celery from there::

  cd src/eukalypse_now
  python manage.py celeryd -E -B -I eukalypse_now.tasks --settings=settings



Starting the Web Service
________________________

run the server!::

  eukalypse_now run_gunicorn 0.0.0.0:8000 -w 3
