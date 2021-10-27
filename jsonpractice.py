import json
import requests

def login(mail, password):
    
    s = requests.Session()
    dictionary = {
        "email": mail,
        "password": password,
        
    }
    res = s.post("example site.com", json=dictionary)
    s.headers.update({"authorization": json.loads(res.content)["token"]})
    print(res.content)
    return s

session = login("example@example.com, qwerty123")