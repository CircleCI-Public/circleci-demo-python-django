# CircleCI Demo Application: Python / Django

[![CircleCI](https://circleci.com/gh/CircleCI-Public/circleci-demo-python-django.svg?style=svg)](https://circleci.com/gh/CircleCI-Public/circleci-demo-python-django)

This is an example application showcasing how to build test and deploy a Django app on CircleCI 2.0.

You can follow along with this project by reading the [documentation](https://circleci.com/docs/2.0/language-python/).

## Features of the demo

- regularly updated to use latest Python and Django (currently Python 3.6.4 and Django 2.0.1)
- uses [pipenv](http://pipenv.readthedocs.io/en/latest/) to install and manage dependencies and virtualenvs on CircleCI
- shows usage of caching on CircleCI 2.0 to speed up builds. Makes use of Ppipfile.lock to invalidate cache if dependencies change
- runs tests against a PostgreSQL database
- store and upload test result in Junit XML format with [unittest-xml-reporting](https://github.com/xmlrunner/unittest-xml-reporting) to enable Test Summary and Insights on CircleCI

## About the app: django_local_library

Tutorial "Local Library" website written in Django. This is based on the excellent [MDN Django tutorial.](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website).

----

This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

* There are models for books, book copies, genre, language and authors.
* Users can view list and detail information for books and authors.
* Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
* Librarians can renew reserved books

![Local Library Model](https://github.com/mdn/django-locallibrary-tutorial/blob/master/catalog/static/images/local_library_model_uml.png)

## License Information

Documentation (guides, references, and associated images) is licensed as Creative Commons Attribution-NonCommercial-ShareAlike CC BY-NC-SA. The full license can be found [here](http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode), and the human-readable summary [here](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Everything in this repository not covered above is licensed under the [included CC0 license](LICENSE).

