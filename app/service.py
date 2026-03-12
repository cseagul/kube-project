import requests, json
from app.config import API_URL, API_TIMEOUT

def fetch_data():
    response = requests.get(API_URL, timeout=API_TIMEOUT)
    print(API_TIMEOUT)
    response.raise_for_status()
    results = response.json()['results']
    extracted_list = [
                        { 'name': character['name'], 'location': character['location']['name'], 'imageLink': character['image']} 
                        for character in results
                    ]

    return json.dumps(extracted_list)

if __name__ == "__main__":
    data = fetch_data()
    print(data)