# Django Blogging App

A simple blogging application built with Django, created as a project to practice core Django concepts.

## Starting the application locally

Make sure you have Python and [Django installed](https://www.djangoproject.com/download/)
```bash
python --version
python -m pip show django
```

Clone the repository:
```bash
git clone git@github.com:amandahamynen/django-blogging-app.git
cd django-blogging-app
```

Apply migrations and run the app:
```bash
python manage.py migrate
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

## Admin panel

Create a superuser:
```bash
python manage.py createsuperuser
```

Follow the prompts to set a username and password.
Access the admin panel at:

http://127.0.0.1:8000/admin

## Development notes

When you make changes to models, create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

