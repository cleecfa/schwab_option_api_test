from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Schwab API Financial Web '

@app.route('/api-key')
def get_api_key():
    # Example endpoint to show API key is loaded (do not use in production)
    api_key = os.getenv('SCHWAB_API_KEY', 'Not Set')
    return jsonify({'api_key': api_key})

if __name__ == '__main__':
    app.run(debug=True)
