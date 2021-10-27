import json
import requests

def login(email, password):
    
    m = requests.Session()
    dictionary = {
        "email": email,
        "password": password,
        
    }
    res = m.post("example site.com", json=dictionary)
    m.headers.update({"authorization": json.loads(res.content)["token"]})
    print(res.content)
    return m

session = login("example@example.com, qwerty123")
