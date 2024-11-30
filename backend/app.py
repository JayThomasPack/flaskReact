


import os
from flask import Flask
from api.routes.urls import urls_bp
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(urls_bp, url_prefix="/api")

@app.route('/')
def index():
    return "Welcome to the Flask API"

if __name__ == '__main__':
    app.run(debug=True)





