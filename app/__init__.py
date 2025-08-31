from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

# Simplified CORS configuration - allow all for now
CORS(app, origins=[
    'https://voice-grocery-ai-frondend.vercel.app',
    'https://voice-grocery-ai-frontend.vercel.app', 
    'http://localhost:3000',
    'http://localhost:5173',
    '*'  # Allow all origins for testing
], methods=['GET', 'POST', 'OPTIONS'], allow_headers=['Content-Type'])

from app import routes
