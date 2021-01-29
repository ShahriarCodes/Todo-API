# Todo-API

The second project from the book **Django for APIs - Build web APIs with Python and Django** \
by _William S. Vincent_ \
Get the book at [here](http://leanpub.com/djangoforapis)

# Installation

First clone the repo

```
$ git clone https://github.com/shahriar100/Todo-API/
```

**Backend** 

To install Pipenv we can use pip3 which Homebrew automatically installed for us alongside Python 3.

```
$ pip3 install pipenv
```

Cd into the directory and install dependecies from piplock

```
$ cd Todo-API/backend
$ pipenv install
```

If you look within our directory there are now two premade files: Pipfile and Pipfile.lock. We have the information we need for a new virtual environment but we have not activated it yet. Let’s do that with pipenv shell.

```
$ pipenv shell
```

If you are on a Mac you should now see parentheses around the name of your current directory on your command line which indicates the virtual environment is activated. Since we’re in a Todo-API directory that means we should see (Todo-API) at the beginning of the command line prompt. Windows users will not see the shell prompt.

```
(Todo-API) $
```

This means it’s working! Now migrate the database and run the server

```
(Todo-API) $ python nanage.py makemigrations
(Todo-API) $ python nanage.py migrate
(Todo-API) $ python nanage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 22, 2021 - 02:18:54
Django version 2.2.6, using settings 'todo_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

**Frontend**

Keep the django server running inside a console window and open another console to start the react server

```
$ cd Todo-API/frontend
```

Install dependencies and start the server

```
$ yarn install
$ yarn start
```

Working directory structure

```
(Todo-API) $ tree
.
├── backend
│   ├── db.sqlite3
│   ├── manage.py
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── todo_project
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── todos
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   └── __init__.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── frontend
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── README.md
│   ├── src
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── reportWebVitals.js
│   │   └── setupTests.js
│   └── yarn.lock
└── README.md

7 directories, 37 files


```
