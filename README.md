# django_pet_adoption

A repo for practicing Python Django

## Requirements
- Python 3
- Django

## Commands
Create a virtual environment for this project to separate its dependencies from other Python project.
Below are the commands for virtualenv:
```
# Install virtualenv
pip install virtualenv

# Navigate to the path where you went to store your virtual environments
cd [path-to-environments]

# Create a virtual environment
virtualenv [envname] # create a Python 2 environment
virtualenv -p python3 [envname] # for Python 3

# Use the virtual environment
source [path-to-envname]/bin/activate

# This will deactivate virtual environment
deactivate
```

Install Python dependencies:
```
pip install -r requirement.txt
```

To start a new project:
```
django-admin startproject [projectname]
```

To run the server:
```
python manage.py runserver
```

Start a new app inside the project folder:
```
python manage.py startapp [appname]
```

To activate a newly created app, go to [projectname]/settings.py and add `'appname'` in the INSTALLED_APPS list.

### Migration
When there are changes in the model, you need to first generate the migration files to make the database match the model:
```
python manage.py makemigrations
```
Then run migrations to make changes effective:
```
# Run all migrations
python manage.py migrate
# Run migrations on a specific app
python manage.py migrate [appname] [number]
```
To import pet.csv data into the database, run:
```
python import.py
```

## Troubleshooting
1. If encountered errors when running migration, delete everything except the `__init__.py` inside the `migrations` folder and then run `python manage.py makemigrations`.
