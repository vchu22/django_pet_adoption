# djangopractice

A repo for practicing Python Django

### Commands
Install Django:
```
pip3 install django
```

To start a new project:
```
django-admin startproject projectname
```

To run the server:
```
python3 manage.py runserver
```

Start a new app inside the project folder
```
python3 manage.py startapp appname
```

To activate a newly created app, go to [projectname]/settings.py and add `'appname'` in the INSTALLED_APPS list.
