from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
# CORS configuration for production and development
if os.getenv('RENDER_ENV') == 'production':
    # Production CORS - allow broader access for testing
    CORS(app, origins=[
        'https://your-frontend-domain.onrender.com',  # Update this after frontend deployment
        '*',  # Temporary: allow all origins for testing
    ])
else:
    # Development CORS - allow localhost
    CORS(app, origins=[
        'http://localhost:3000',
        'http://localhost:5173',
        'http://localhost:4173',
        'http://localhost:8080',
        'http://localhost:8081',
        'http://127.0.0.1:3000',
        'http://127.0.0.1:5173',
        'http://127.0.0.1:4173',
        'http://127.0.0.1:8080',
        'http://127.0.0.1:8081'
    ])

from app import routes
