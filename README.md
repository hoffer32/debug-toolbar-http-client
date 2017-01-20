# debug-toolbar-http-client
A django debug toolbar panel which records http requests made by app. It's simple base on [vcrpy](https://github.com/kevin1024/vcrpy) which will decompress “gzip” and “deflate” response bodies before recording

![alt tag](https://github.com/hoffer2github/debug-toolbar-http-client/blob/master/sample.png)


##Usage

###. Install and configure [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)

###. Install Django Debug Toolbar HTTP Client Panel:

```
    pip install django-debug-toolbar-http-client
```

###. Add ``http_client_panel`` to your ``INSTALLED_APPS`` setting:

```

    INSTALLED_APPS = (
        # ...
        'http_client_panel',
    )
```

###. Add HTTP Client Panel to Django Debug Toolbar middleware:

```
    MIDDLEWARE_CLASSES = (
        ...
        'http_client_panel.panels.HttpClient.HttpClientPanel',
        ...
    )
```
