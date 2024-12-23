from flask import jsonify


ACCESS_DENIED_ERROR = jsonify({"error": "Access denied"}), 403
