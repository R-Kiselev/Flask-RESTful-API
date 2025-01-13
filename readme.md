# Flask-restful API

This project implements RESTful API for a simple banking system.
Inspired by the structure and some solutions from the [cookiecutter-flask-restful](https://github.com/karec/cookiecutter-flask-restful) project.

## Features

* Simple flask application using application factory, blueprints
* Simple pagination utils
* Simple cli implementation with basics commands (init, run, etc.)
* [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) included in entry point
* RBAC using [Flask-JWT-Extended](http://flask-jwt-extended.readthedocs.io/en/latest/) 
* Configuration using environment variables

## Main libraries used

* [Flask](http://flask.pocoo.org/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) 
* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/index.html)
* [Flask-JWT-Extended](http://flask-jwt-extended.readthedocs.io/en/latest/)
* [dotenv](https://github.com/theskumar/python-dotenv)

## Usage

* [Project structure](#Project-structure)
* [Installation](#Installation)
* [Configuration](#Configuration)
* [Authentication](#Authentication)
* [Using docker-compose](#using-docker-compose)
* [Makefile](#makefile-usage)
* [CRUD operations examples](#CRUD-operations-examples)

## Project structure
    ```
    .
    │
    ├── app/                   
    │   ├── api/
    │   │   ├── resources/
    │   │   │   ├── accounts.py
    │   │   │   ├── ...
    │   │   ├── schemas/
    │   │   │   ├── account.py
    │   │   │   ├── ...
    │   │   └── views.py
    │   ├── auth/
    │   │   ├── utils.py
    │   │   └── views.py 
    │   ├── commons/
    │   │   ├── base_resources.py
    │   │   ├── validation_utils.py
    │   │   └── pagination.py
    │   ├── models/
    │   │   ├── account.py
    │   │   ├── ...
    │   │── app.py
    │   │── config.py
    │   │── error_handling.py
    │   │── extensions.py
    │   └── flask_cli.py
    ├── wsgi.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    ├── .dockerignore
    ├── Makefile
    ├── entrypoint.sh
    ├── requirements.txt
    └── .env
    ```

- **app/** ── Root directory for the Flask application code.
  - **api/** ── Defines API logic and structure.
    - **resources/** ── Contains RESTful resources for different API endpoints.
    - **schemas/** ── Contains Marshmallow schemas for data serialization and validation.
    - **views.py** ── Registers API blueprint and endpoint routes.
  - **auth/** ── Manages authentication and authorization logic.
    - **utils.py** ── Contains utility functions for RBAC and JWT handling.
    - **views.py** ── Registers `auth` blueprint and endpoint routes related to authentication.
  - **commons/** ── Holds reusable utilities and shared components.
    - **base_resources.py** ── Provides base classes for API resources.
    - **validation_utils.py** ── Includes helper functions for data validation.
    - **pagination.py** ── Implements pagination utilities for API responses.
  - **models/** ── Defines database models for application entities.
  - **app.py** ── Implements the Flask application factory and initializes the app.
  - **config.py** ── Contains configuration settings for different flask environments.
  - **error_handling.py** ── Manages Flask app error handling and logs exceptions.
  - **extensions.py** ── Initializes and configures Flask extensions (e.g., SQLAlchemy, Marshmallow).
  - **flask_cli.py** ── Defines custom Flask CLI commands for tasks like app init.
- **wsgi.py** ── Entry point for running the Flask application.
- **requirements.txt** ── Lists Python dependencies required for the project.
- **.env** ── Stores environment variables for secure configuration.
- **Dockerfile** ── Defines the application container image.
- **docker-compose.yml** ── Manages the application container and its dependencies.
- **Makefile** ── Automates repetitive tasks like starting the app.
- **entrypoint.sh** ── Contains the entrypoint script for the Docker container.

## Installation

### Create project
1. Clone repository.
2. Create python venv
3. pip install -r requirements.txt
4. Init MySQL database on your computer.
5. Configure .env file

## Configuration
Configuration is handled by environment variables, for development purpose you just need to create and add entries in `.env` file.

It should consist of the following variables:
```
MYSQL_DATABASE = 'mybank'
MYSQL_ROOT_PASSWORD = 'pass'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@db:3306/mybank'

FLASK_ENV = 'development'
FLASK_APP = 'app.app:create_app'
FLASK_CERT = 'adhoc'
SECRET_KEY = 'SECRET'
JWT_SECRET_KEY = "JWT_SECRET"

DEFAULT_ROLE = 'user'

ADMIN_EMAIL = 'admin@gmail.com'
ADMIN_PASS = 'password'
```

You can configure database connection by setting `SQLALCHEMY_DATABASE_URI` in `.env` file.
It is crucial to set the correct database URI to connect to your database.
Escpecially when you are using docker-compose, you should set the host to `db` which is the name of the service in the docker-compose file.
If you want to run the application on your local machine, you should set the host to `localhost`.

`FLASK_ENV` is set to `development` by default. This automatically enables debug mode and changes errorhandlers behavior (look at `config.py`).

## Authentication

### Registration

POST https://localhost:5000/auth/register

HEADERS
```json
{
    Content-Type: application/json
}
```

REQUEST
```json
{
    "email" : "exampleuser@gmail.com",
    "password" : "password"
}
```

RESPONSE
```json
201 CREATED
{
    "item": {
        "email": "exampleuser@gmail.com",
        "id": 62,
        "is_blocked": false,
        "roles": [
            "user"
        ]
    },
    "msg": "item created"
}
```

### Login

To access protected resources, you will need an access token. You can generate an access and token using `/auth/login` endpoint. 
Created access token contains client id, account id's in jwt claims if they exists.

POST https://localhost:5000/auth/login

HEADERS
```json
{
    Content-Type: application/json
}
```

REQUEST
```json
{
    "email" : "admin@gmail.com",
    "password" : "password"
}
```

RESPONSE
```json
200 OK
{
    "access_token": {your_token}
}
```

## Using docker-compose

You can use docker-compose to run the application in a containerized environment.
Also, you can use the Makefile to automate repetitive tasks.
At first, you need to initialize your environment by running the following commands. 
This will create containers and initialize the database.

With docker-compose
```bash
docker-compose build
docker-compose up
docker exec -it <backend_container_id> flask init
docker exec -it <backend_container_id> flask db-init
docker exec -it <backend_container_id> flask db-migrate
docker exec -it <backend_container_id> flask db-upgrade
```

With docker-compose and the Makefile
```bash
make init
```

Now your project is ready to use.

## Makefile usage

Initizalize the environment
```bash
make init
```

Build the containers
```bash
make build
```

Run the containers
```bash
make run
```

Create migrations folder
```bash
make db-init
```

Create new database migration
```bash
make db-migrate
```

Apply database migrations
```bash
make db-upgrade
```

## CRUD operations examples

If user don't have access to endpoint, he will receive 403 Forbidden status code.
This can be caused by :
* trying to access endpoint without token
* if user has wrong role
* if user is not owner of the resource

RESPONSE
```json
403 Forbidden
{
    "msg": "Access denied"
}
```

GET https://localhost:5000/api/accounts/1/cards

HEADERS
```json
{
    Authorization : Bearer {{token}}
}
```

RESPONSE
```json
200 OK
{
    "total": 4,
    "pages": 1,
    "next": "/api/accounts/1/cards?page_number=1&page_size=5",
    "prev": "/api/accounts/1/cards?page_number=1&page_size=5",
    "results": [
        {
            "id": 1,
            "balance": 300,
            "account_id": 1
        },
        {
            "id": 2,
            "balance": 500,
            "account_id": 1
        },
        {
            "id": 5,
            "balance": 500,
            "account_id": 1
        },
        {
            "id": 7,
            "balance": 500,
            "account_id": 1
        }
    ]
}
```
POST https://localhost:5000/api/accounts/1/cards

HEADERS
```json
{
    Authorization : Bearer {{token}}
}
```

REQUEST
```json
{
    "balance" : 520
}
```

RESPONSE
```json
201 CREATED
{
    "msg": "item created",
    "item": {
        "id": 8,
        "balance": 520,
        "account_id": 1
    }
}
```

PUT https://localhost:5000/api/accounts/cards/1

HEADERS
```json
{
    Content-Type : application/json,
    Authorization : Bearer {{token}}
}
```

REQUEST
```json
{
    "balance" : 600
}
```

RESPONSE
```json
200 OK
{
    "msg": "item updated",
    "item": {
        "id": 1,
        "balance": 600,
        "account_id": 1
    }
}
```
DELETE https://localhost:5000/api/accounts/cards/1

HEADERS
```json
{
    Authorization : Bearer {{token}}
}
```

RESPONSE
```json
200 OK
{
    "msg": "item deleted",
    "item": {
        "id": 1,
        "balance": 600,
        "account_id": 1
    }
}
```

Other resources are similar to Cards endpoints.