from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

# CORS configuration for production and development
CORS(app, 
     origins=[
         'https://voice-grocery-ai-frondend.vercel.app',  # Your frontend domain
         'https://voice-grocery-ai-frontend.vercel.app',  # Alternative spelling
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
     ],
     methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
     allow_headers=['Content-Type', 'Authorization'],
     supports_credentials=True
)

from app import routes
