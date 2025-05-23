import os
import requests
from dotenv import load_dotenv

load_dotenv()

SCHWAB_API_KEY = os.getenv('SCHWAB_API_KEY')
SCHWAB_API_SECRET = os.getenv('SCHWAB_API_SECRET')

# Example: Replace with actual Schwab API endpoint and parameters
def get_sample_data():
    url = 'https://api.schwab.com/v1/example-endpoint'  # Replace with real endpoint
    headers = {
        'Authorization': f'Bearer {SCHWAB_API_KEY}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    data = get_sample_data()
    if data:
        # Basic exploratory data analysis
        print('Keys in response:', list(data.keys()))
        print('First 500 characters of response:')
        print(str(data)[:500])
    else:
        print('No data received.')

if __name__ == '__main__':
    main()
