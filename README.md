# debug-toolbar-http-client
A django debug toolbar panel which records http requests maked by app.

![alt tag](https://github.com/hoffer2github/debug-toolbar-http-client/blob/master/sample.png)


Installation
============

#. Install and configure `Django Debug Toolbar <https://github.com/django-debug-toolbar/django-debug-toolbar>`_

#. Install Django Debug Toolbar HTTP Client Panel:

   .. code-block:: bash

    pip install django-debug-toolbar-http-client

#. Add ``http_client_panel`` to your ``INSTALLED_APPS`` setting:

   .. code-block:: python

    INSTALLED_APPS = (
        # ...
        'http_client_panel',
    )

#. Add HTTP Client Panel to Django Debug Toolbar middleware:

   .. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'http_client_panel.panels.HttpClient.HttpClientPanel',
        ...
    )
