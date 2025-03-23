
@echo off
cd /d D:\TurfProject

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install django djangorestframework

echo Creating Django project...
if not exist manage.py (
    django-admin startproject turf_Project .
) else (
    echo Django project already exists, skipping creation...
)

echo Creating Django app...
if not exist turf_app (
    django-admin startapp turf_app
) else (
    echo Django app 'turf_app' already exists, skipping creation...
)

echo Running migrations...
if exist manage.py (
    python manage.py migrate
) else (
    echo Error: manage.py not found in D:\TurfProject
    exit /b 1
)

echo Creating superuser...
set DJANGO_SUPERUSER_USERNAME=turf_admin
set DJANGO_SUPERUSER_EMAIL=admin@turf.com
set DJANGO_SUPERUSER_PASSWORD=turf_pass123
python manage.py createsuperuser --noinput


echo Starting Django server...
python manage.py runserver
