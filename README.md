# CircleCI Demo Application: Python / Django

This is an example application showcasing how to build test and deploy a Django app on CircleCI 2.0.

You can follow along with this project by reading the [documentation](https://circleci.com/docs/2.0/language-python/).

## License Information

Documentation (guides, references, and associated images) is licensed as Creative Commons Attribution-NonCommercial-ShareAlike CC BY-NC-SA. The full license can be found [here](http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode), and the human-readable summary [here](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Everything in this repository not covered above is licensed under the [included CC0 license](LICENSE).




## About the app: django_local_library

Tutorial "Local Library" website written in Django.

----

This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

* There are models for books, book copies, genre, language and authors.
* Users can view list and detail information for books and authors.
* Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
* Librarians can renew reserved books

![](https://github.com/hamishwillee/django_local_library/blob/master/catalog/static/images/local_library_model_uml.png)






For more information see the associated [MDN tutorial home page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website).
