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


Install phantomjs or selenium
----------------------

eukalypse uses phantomjs or selenium to create the images of websites. Please take a look at the documentation how to configure those to your needs. 
As default, eukalypse uses phantomjs and eukalypse_now tries to use the default configuration. You have to install phantomjs beforehand.::

   sudo gem install phantomjs 

.. note:: During tests, selenium + chrome on Linux had the best performance and "correctness" of the images. phantomjs and selenium + firefox on Linux sometimes created false positives due to nondeterministic rendering.

Get eukalypse_now
----------------------

It is available through pip. ::

  pip install eukalypse_now


Settings
--------

Create a custom settings file in ~/.eukalypse_now/ ::

  eukalypse_now init

Check the configuration in ~/.eukalypse_now//eukalypse_now.conf.py and update it to your needs. You can overwrite every configuration you find in the settings.py

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

This daemon runs checks at night.::

   eukalypse_now celeryd -E -B -I eukalypse_now.tasks



Starting the Web Service
________________________

run the server!::

  eukalypse_now run_gunicorn 0.0.0.0:8000 -w 3
