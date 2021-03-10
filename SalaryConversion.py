import json
import urllib.request

with urllib.request.urlopen('http://jsonplaceholder.typicode.com/users') as userUrl:
    user = json.loads(userUrl.read().decode())
    print(user)
    
with open('JSON/salary_data.json') as s:
  salary = json.load(s)

