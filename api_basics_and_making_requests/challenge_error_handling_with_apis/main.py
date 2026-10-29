import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"

    # Write your code here
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError if the request failed
        data = response.json()
        cat_fact = data["fact"]  # May raise KeyError if 'fact' is missing
        print(cat_fact)
    except Exception:
        print("Failed to retrieve cat fact.")

get_cat_fact
 

 