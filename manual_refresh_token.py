import os
from dotenv import load_dotenv

# Load environment variables from .env file
def load_env_vars():
    load_dotenv()
    app_key = os.getenv('SCHWAB_API_KEY')
    app_secret = os.getenv('SCHWAB_API_SECRET')
    callback_url = os.getenv('CALLBACK_URL')
    port = os.getenv('PORT')
    return app_key, app_secret, callback_url, port

if __name__ == '__main__':
    app_key, app_secret, callback_url, port = load_env_vars()
    print(f"SCHWAB_API_KEY: {app_key}")
    print(f"SCHWAB_API_SECRET: {app_secret}")
    print(f"CALLBACK_URL: {callback_url}")
    print(f"PORT: {port}")
