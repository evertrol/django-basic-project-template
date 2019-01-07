This is a simple Django template, that organises the basic Django
project files into subdirectories, to allow for more organised growth
of the project.
It also provides a basic HTML template to build from.

The layout it provides looks as follows:

    manage.py
    <<project-name>>/
      __init__.py
      urls.py
      apps/
        urls.py
        __init__.py
      server/
        wsgi.py
        __init__.py
      settings/
        base.py
        local_template.py
        __init__.py
      staticfiles
        css/
          base.css
      templates/
        base.html
        footer.html
        nav.html
        user.html


Usage
=====

You can use the template with

    django-admin.py startproject --template =https://github.com/evertrol/django-project-template/archive/master.zip <<project-name>>


Requirements
============

Django 2.0 and later.


License
=======

This software is licensed under the MIT license.
