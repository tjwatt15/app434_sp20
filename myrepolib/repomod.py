import requests
import json

#fail= #intentional fail

def myfunc():
    return 1

def print_name(name):
    return f'The name entered is {name}.'

def fake_data():
    return {"one":1, "two":2}

def call_web_service(url="http://localhost:5000/fakedata"):
    res = requests.get(url)
    return json.loads(res.content)