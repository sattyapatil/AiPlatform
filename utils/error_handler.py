from flask import jsonify

from app import app


@app.errorhandler(400)
def bad_request_error(error):
    message = "Bad request"
    return jsonify({"message": message}), 400


@app.errorhandler(401)
def unauthorized_error(error):
    message = "Unauthorized"
    return jsonify({"message": message}), 401


@app.errorhandler(403)
def forbidden_error(error):
    message = "Forbidden"
    return jsonify({"message": message}), 403


@app.errorhandler(404)
def not_found_error(error):
    message = "Resource not found"
    return jsonify({"message": message}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    message = "Method not allowed"
    return jsonify({"message": message}), 405


@app.errorhandler(500)
def internal_server_error(error):
    message = "Internal server error"
    return jsonify({"message": message}), 500
