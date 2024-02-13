from pizzaMng import PizzaManager
from userMng import UserManager
from pizzaHandler import PizzaHandler
import requests
import json

url = 'http://localhost:5000/register'

payload = {

    'username': 'John',
 
    'password' : 'pesandrej11',

    'address' : 'Spanskih boraca 30a'
}

headers = {

    'Content-Type': 'application/json'

}

json_payload = json.dumps(payload)

response = requests.post(url, data=json_payload, headers=headers)

print(response.status_code)