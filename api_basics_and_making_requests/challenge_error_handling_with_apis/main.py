import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.status_code)
        data = response.json()
        print(data["fact"])
    except Exception:
        print("Failed to retrieve cat fact.")

get_cat_fact()