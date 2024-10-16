import logging
from flask import jsonify
from app.extensions import db
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from werkzeug.exceptions import HTTPException

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
    return jsonify({
        "error_type": "Database integrity error",
        "error_message": str(e),
        "additional_info": "Please check your data for constraints violations."
    }), 500

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

def register_api_errorhandlers(blueprint):
    """Return json errors.

    This will avoid having to try/catch errors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status
    """
    blueprint.register_error_handler(HTTPException, handle_http_exception)
    blueprint.register_error_handler(ValidationError, handle_validation_error)
    blueprint.register_error_handler(IntegrityError, handle_database_integrity_error)
    blueprint.register_error_handler(SQLAlchemyError, handle_database_error)
    blueprint.register_error_handler(Exception, handle_general_exception)