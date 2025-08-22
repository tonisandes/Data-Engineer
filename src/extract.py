import requests
import json

def extract_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()

        with open("data/raw/users_raw.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Data extracted and saved to data/raw/users_raw.json")
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")