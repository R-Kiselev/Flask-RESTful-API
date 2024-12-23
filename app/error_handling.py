import os
import logging

from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from werkzeug.exceptions import HTTPException

from app.extensions import db

ENV = os.getenv('FLASK_ENV', 'production').lower()

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(f"{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def handle_validation_error(e):
    logger.error(f"Validation Error: {str(e)}")
    return jsonify({"error_type": "Validation Error", "error_message": e.messages}), 400


def handle_database_integrity_error(e):
    db.session.rollback()
    logger.error(f"Database Integrity Error: {str(e)}")

    if ENV == 'development':
        error_message = str(e) 
    elif "Duplicate" in str(e):
        error_message = "An item with the same value already exists."
    else:
        error_message = "Input data is invalid. Please check the input data." 

    return jsonify({
        "error_type": "Database Integrity error",
        "error_message": error_message
    }), 409 if "Duplicate" in str(e) else 500


def handle_database_error(e):
    db.session.rollback()
    logger.error(f"Database Error: {str(e)}")
    return jsonify({"error_type": "Database error", "error_message": str(e)}), 500


def handle_http_exception(e):
    logger.error(f"HTTP Error: {str(e)}")
    return jsonify({"error_type": "Http error", "error_message": e.description}), e.code


def handle_general_exception(e):
    logger.error(f"General Error: Type={type(e).__name__}, Message={str(e)}")
    return jsonify({"error_type": type(e).__name__, "error_message": str(e)}), 500


def register_app_errorhandlers(app):
    """Return json errors.

    This will avoid having to try/catch errors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status
    """
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(IntegrityError, handle_database_integrity_error)
    app.register_error_handler(SQLAlchemyError, handle_database_error)
    app.register_error_handler(Exception, handle_general_exception)
