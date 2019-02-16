python-scratch
==============

.. image:: https://img.shields.io/pypi/v/python-scratch.svg
    :target: https://pypi.python.org/pypi/python-scratch
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/pladdy/python-scratch.png
   :target: https://travis-ci.org/pladdy/python-scratch
   :alt: Latest Travis CI build status

Me learning python

Goals
-----
- Use/learn python 3
- do work in a isolated environment (meaning libraries aren't installed globally, but locally like you can with bundler in ruby)
- see how testing works in python

Usage
-----
.. code:: bash

  git clone git@github.com/pladdy/python_scratch
  cd python_scratch
  make
  make test

Installation
------------
`make`

The make file assumes you're using a mac with homebrew.

How I set up the repo
---------------------
I installed python3 via brew:

.. code:: bash

  brew install python3

Then I added some aliases to my .alias file:

.. code:: bash

  alias pip='pip3'
  alias python='python3'

Then I installed cookiecutter and used a cookiecutter template to create the project:

* Reference: https://github.com/kragniz/cookiecutter-pypackage-minimal

.. code:: bash

  pip install cookiecutter
  git clone https://github.com/kragniz/cookiecutter-pypackage-minimal.git
  cookiecutter cookiecutter-pypackage-minimal/
  # followed the prompts and made this shiny pile of bits


Then I decided on using virtualenv for my environment control.  I based this on some stack overflow reading and finally just going through this: https://docs.python-guide.org/dev/virtualenvs/

At this point I had a project, so I started using pipenv to do the things.  I had to install pipenv first, then used it to install other things.  This ends up creating a Pipfile of dependencies which I checked in.

Now one can just use `make` and dependencies should be taken care of with pipenv and the Pipfile.

.. code:: bash

  pip install pipenv
  pipenv install cookiecutter
  pipenv install sphinx
  pipenv install pipenv
  pipenv install pytest
  pipenv install pytest-cov
  pipenv install pylama
  pipenv install pylama-pylint

Using virtualenv
^^^^^^^^^^^^^^^^
Using the virtual environment manually:

.. code:: bash

  source venv/bin/activate
  # do some stuff in a virtual python env
  deactivate

Add aliases to make this less verbose:

.. code:: bash

  vim ~/.aliases
  alias act='source venv/bin/activate'
  alias deact='deactivate'

Requirements
^^^^^^^^^^^^
* homebrew
* python3
* pip3
* pandoc

References
----------
* Python Guide: https://docs.python-guide.org/
    * It covers a lot of topics from tools like logging, build/deploy, concurrency, etc.
* Testing with pytest: https://docs.pytest.org/en/latest/
* Documenting Tool: http://www.sphinx-doc.org/en/master/

Compatibility
-------------

Licence
-------

See LICENSE

Authors
-------

`python-scratch` was written by `Matt Pladna <pladdypants@gmail.com>`_.
