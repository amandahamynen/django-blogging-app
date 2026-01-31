# Django Blogging App

A simple blogging application made with Django.

## Starting the application locally

Make sure you have [Django installed](https://www.djangoproject.com/download/)
```bash
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

Access the app:

http://127.0.0.1:8000/

## Developing the application

Create new migrations based on the changes you have made to your models and apply them
```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser:
```bash
python manage.py createsuperuser
```

Enter the Username and Password you set while creating the superuser at admin panel


http://127.0.0.1:8000/admin/


