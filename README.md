Restaurand-api
==============

API and backend for restaurand application (https://github.com/dflorent/restaurand).

Prerequisites
-------------

- Python
- Virtalenv
- Heroku user account
- Postgres

Start the app
-------------

```
source venv/bin/activate
foreman s -f Procfile.dev
```

You can view the application by navigating to http://127.0.0.1:8000/ in your browser.

Dependencies
------------

Specify dependencies to Heroku with Pip.

```
pip freeze > requirements.txt
```

Installing dependencies with this following command.

```
pip install -r requirements.txt
```

Django settings
---------------

```
# example local_settings.py
# path/to/app/local_settings.py

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypwd',
        'HOST': 'localhost',
    }
}
```

Environment variables
---------------------

```
# root/path/.env

SECRET_KEY=my_secret_key
```

Deploy to Heroku
----------------

```
git push heroku master
```
