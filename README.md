# DJANGO - REACT - APP - API

-   [Front end REACT link](https://jess-django-react-app.herokuapp.com)
-   [Backend end API link](https://jess-django-react-api.herokuapp.com/graphql/)

## Features

-   Django - [documentation](https://docs.djangoproject.com/en/3.2/)
-   GraphQL - [documentation](https://www.howtographql.com)
-   Graphene-Django - [documentation](https://docs.graphene-python.org/projects/django/en/latest/)
-   JWT login [documentation](https://github.com/flavors/django-graphql-jwt)
-   Cors headers
-   Todo CRUD
-   Like - User Voting
-   Search Feature

## Installation

---

### DJANGO

#### create virtual environment

```console
mkdir django-react-api && cd "$_"
pipenv shell
```

#### install django and other libraries

```console
pipenv install django graphene-django django-graphql-jwt django-cors-headers
```

#### install code formatter - autopep8

```console
pipenv install --dev autopep8
```

#### start django project

```console
django-admin startproject app .
```

#### initialize django default settings

```console
python manage.py migrate
```

## TODO APP

#### create todo app

```console
python manage.py startapp todo
```

#### apply all defined model - [documentation](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

```console
python manage.py makemigrations
python manage.py migrate
```

#### apply specific defined model

```console
python manage.py makemigrations todo
python manage.py migrate todo
```

#### Adding data via shell

```console
python manage.py shell
>>> from todo.models import Todo
>>> Todo.objects.create(title="Todo 1", description="Todo 1 Description", url="https://www.todo1.com")
```

### GRAPHENE

#### Add graphene_django in settings.py.

-   [see documentation](https://docs.graphene-python.org/projects/django/en/latest/installation/)

```python
INSTALLED_APPS = [
    ...
    'graphene_django',
    'todo',
]
GRAPHENE = {
    'SCHEMA': 'app.schema.schema'
}
```

### SCHEMA

-   create schema.py (general schema) in app, todo folder
-   [see documentation](https://docs.graphene-python.org/projects/django/en/latest/schema/)

### MUTATION

-   add create mutation CreateTodo in todo/schema.py
-   [see documentation](https://docs.graphene-python.org/projects/django/en/latest/mutations/)

#### Add graphql csrf to the urls.py

```python
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    ...
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
```

### USER

-   Add user/schema.py shema and mutation
-   Import user schema in app schema

### JWT Login

-   JSON Web Token authentication for Django GraphQL
-   Install [Django GraphQL JWT](https://github.com/flavors/django-graphql-jwt)

### CRUD

-   Create Update Schema with Authorization

#### run django

```
python manage.py runserver
```

---

## GRAPHQL

-   [API Client](https://insomnia.rest/download) - Leading Open Source API Client, and Collaborative API Design Platform for REST, SOAP, GraphQL, and GRPC.

## HEROKU

-   [Deployment Guide](https://devcenter.heroku.com/articles/django-app-configuration) - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

---

## TODO

- [x] Add a todo search feature
- [ ] Add Tags assigned to Todo
- [ ] Add exisiting tags to todo
- [ ] Filter Todo list by Tags
- [ ] Add a line graph of todo count and completed todo per day
- [ ] Manage role who can view others todos
- [ ] Dockerize this app
- [ ] [Make Django Production Ready](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
