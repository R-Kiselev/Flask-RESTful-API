# Flask-restful API

This project implements RESTful API for a simple banking system. 

## Features

* Simple flask application using application factory, blueprints
* Simple pagination utils
* Configuration using environment variables

## Main libraries used

1. Flask ─ A lightweight web framework for building web applications.
2. Flask-RESTful ─ A library that simplifies building RESTful APIs with Flask.
3. Flask-SQLAlchemy ─ Adds support for SQLAlchemy ORM, enabling database interaction.
4. PyMySQL ─ A MySQL client library for Python, used to connect to MySQL databases.
5. marshmallow ─ A library for data serialization and validation, useful for API schemas.
6. python-dotenv ─ Reads key-value pairs from a .env file and can set them as environment variables. 

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
    │   │   ├── error_handling.py
    │   │   └── views.py
    │   ├── commons/
    │   │   ├── base_resources.py
    │   │   └── pagination.py
    │   ├── models/
    │   │   ├── account.py
    │   │   ├── ...
    │   │── app.py
    │   │── config.py
    │   └── extensions.py
    ├── wsgi.py
    ├── requirements.txt
    └── .env
    ```

* **resources** ── Defines RESTful resources for different API endpoints.
* **schemas.py** ── Contains Marshmallow schemas for data serialization and validation.
* **error_handling.py** ── Manages error handling and logging for the API.
* **views.py** ── Registers API blueprint and endpoint routes.
* **commons/** ── Holds reusable utilities.
* **models/** ── Defines database models for the application entities.
* **app.py** ── Holds flask application factory.
* **config.py** ── Holds configuration settings for the application.
* **wsgi.py** ── Entry point for running the Flask application.
* **requirements.txt** ── Lists dependencies required for the project.
* **.env** ── Stores environment variables for secure configuration.

## Installation

### Create project
1. Clone repository.
2. Create python venv
3. pip install requirements.txt
4. Init database on your computer.
5. Configure .env file
6. Start server by running app.py file or using command: "python app.py"

### Configuration
Configuration is handled by environment variables, for development purpose you just
need to update / add entries in `.env` file.

It's filled by default with following content:

```
SQLALCHEMY_DATABASE_URI = 'dialect+driver://username:password@host:port/database'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
```
Available configuration keys (for now):

* `DATABASE_URI`: SQLAlchemy connection string, ex. 'mysql+pymysql://root:pass@localhost/mybank'

## Usage

Postman is used to work with the program.
Query parameters are supported in CRUD operations.
You can paginate data using **page**, **per_page** and table fields.

### Bank resources
GET https://localhost:5000/api/accounts/1/cards

RESPONSE
```json
200 OK
{
    "total": 4,
    "pages": 1,
    "next": "/api/accounts/1/cards?page=1&per_page=5",
    "prev": "/api/accounts/1/cards?page=1&per_page=5",
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

RESPONSE
```json
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