# Flask-restful API

This project implements RESTful API for a simple banking system. 

## Main libraries used

1. Flask-RESTful ── restful API library.
2. Flask-SQLAlchemy ── adds support for SQLAlchemy ORM.
3. PyMySQL ── used to work with MySQL database

## Project structure
```
.
│
├── resources/                   
│   ├── accounts/
│   │   ├── model.py
│   │   └── resource.py
│   ├── banks/
│   │   ├── model.py
│   │   └── resource.py
│   │── ...
│   └── base_resource.py
├── app.py
├── requirements.txt
├── db_settings.py
```

* **resources** ── holds all resources.
* **base_resource.py** ── contains a base class from which all resources are inherited.
* **model.py** ── database table model.
* **resource.py** ── class representing an API methods.
* **app.py** ── flask application initialization.
* **db_settings.py** ── database settings required for the application.

## Running

1. Clone repository.
2. Create python venv
3. pip install requirements.txt
4. Create MySQL database on your computer.
5. In db_settings.py change SQLALCHEMY_DATABASE_URI
6. Start server by running app.py file or using command: "python app.py"

## Usage

Postman is used to work with the program.
Query parameters are supported in CRUD operations.
You can filter data using **limit**, **offset** and table fields.

### Bank resources
GET https://localhost:5000/banks?offset=6&limit=2

RESPONSE
```json
{
    "table_name": "Bank",
    "total": 2,
    "items": [
        {
            "id": 7,
            "name": "Bank of America"
        },
        {
            "id": 8,
            "name": "Bank of China"
        }
    ]
}
```
POST https://localhost:5000/banks

REQUEST
```json
{
    "name" : "Deutsche Bank"
}
```

RESPONSE
```json
{
    "id": 13,
    "name": "Deutsche Bank"
}
```

PUT https://localhost:5000/banks/13

REQUEST
```json
{
    "name" : "Bank of Germany"
}
```

RESPONSE
```json
{
    "id": 13,
    "name": "Bank of Germany"
}
```
DELETE https://localhost:5000/banks/13

RESPONSE
```json
{
    "id": 13,
    "name": "Bank of Germany"
}
```

Other resources are similar to Banks endpoint.