# Django CheatSheet

## Admin commands

**Create Project:** `django-admin.py startproject mysite`

**Check prior deploy:** `python manage.py check`

**Setup/update db:** `python manage.py migrate`

**Generate update db file:** `python manage.py makemigrations app_xxx`

**Generate update db SQL:** `python manage.py sqlmigrate app_xxx 0001`

**Run server:** `python manage.py runserver [ip[:port]]`

**Create app:** `python manage.py startapp app_xxx`

**Start shell:** `python manage.py shell`

**Create admin superuser:** `python manage.py createsuperuser`

## Locations

**Config file:** `mysite/settings.py`

## DB

### DB engines

- **sqlite:** `django.db.backends.sqlite3`
- **mysql:** `django.db.backends.mysql`
- **postgre:** `django.db.backends.postgresql_psycopg2`

## Add new app

- Create new app `python manage.py startapp app_xxx`
- Add app name `app_xxx` to `INSTALLED_APPS` in `mysite/settings.py`
- Generate update db file `python manage.py makemigrations app_xxx`
- Apply `python manage.py migrate`

## Useful doc links

- [Django Ref](https://docs.djangoproject.com/en/1.7/ref/)
- [Admin commands](https://docs.djangoproject.com/en/1.7/ref/django-admin/)
- [Django settings](https://docs.djangoproject.com/en/1.7/topics/settings/)
- [URLs dispatcher](https://docs.djangoproject.com/en/1.7/topics/http/urls/)
- [Model API](https://docs.djangoproject.com/en/1.7/ref/models/instances/)
- [Model fields](https://docs.djangoproject.com/en/1.7/ref/models/fields/)
- [DB related](https://docs.djangoproject.com/en/1.7/topics/db/)
- [Time Zones](https://docs.djangoproject.com/en/1.7/topics/i18n/timezones/)
- [Generic views](https://docs.djangoproject.com/en/1.7/topics/class-based-views/)
- [UT in Django](https://docs.djangoproject.com/en/1.7/topics/testing/)
- [Regex](https://docs.python.org/3/library/re.html#module-re)
- [Static files](https://docs.djangoproject.com/en/1.7/howto/static-files/)
- [Static files ref](https://docs.djangoproject.com/en/1.7/ref/contrib/staticfiles/)
- [WSGI deploy (prod)](https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/)
- [Reusable apps](https://docs.djangoproject.com/en/1.7/intro/reusable-apps/)