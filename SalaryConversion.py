import json
import urllib.request

with urllib.request.urlopen('http://jsonplaceholder.typicode.com/users') as userUrl:
    user = json.loads(userUrl.read().decode())
    #print(user)
    
with open('JSON/salary_data.json') as s:
  salary = json.load(s)

del user[0]['company']
del user[0]['website']
user[0].update({'salaryInIDR': 'another_value'})
user[0].update({'salaryInUSD': 'another_value'})
print(user[0])

with open('user.json', 'w') as json_file:
  json.dump(user, json_file)
