#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
import os
from flask import Flask, make_response, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Register the blueprint for API views
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the storage on teardown"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors that returns a JSON response"""
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == '__main__':
    # Get the host and port from environment variables, with defaults
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    # Run the Flask app
    app.run(host=host, port=port, threaded=True)
