# api link: https://official-joke-api.appspot.com/jokes/random :)

#{
#  "type": "programming",
#  "setup": "Why was the font always tired?",
#  "punchline": "It was always bold.",
#  "id": 443
#}


import requests as rq

def get_random_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = rq.get(url)
    if response.status_code == 200: # if it is successful i go on
        joke_data = response.json()
        tipe = joke_data.get("type", "No type found.")
        setup = joke_data.get("setup", "No setup found.")
        punchline = joke_data.get("punchline", "No punchline found.")
        id = joke_data.get("id", "(Sorry, no ID found.)") # id check
        return f"You founded a {tipe} joke!\n\n{setup}\n{punchline}\n\nThis is joke number {id}. I hope you liked it"
    else:
        return "Failed to retrieve a joke."
    
print(get_random_joke())