import json
import urllib.request
from currency_converter import CurrencyConverter

with urllib.request.urlopen('http://jsonplaceholder.typicode.com/users') as userUrl:
    users = json.loads(userUrl.read().decode())

with urllib.request.urlopen('https://v6.exchangerate-api.com/v6/af83cf7542205b242e8041b8/latest/IDR') as conversion:
    conv = json.loads(conversion.read().decode())

with open('JSON/salary_data.json') as s:
  salary = json.load(s)

"""
for i in salary["array"]:
  print(i['id'])
  print(i["salaryInIDR"])
"""
for user in users:

  user.update(salary["array"][user['id']-1])
  del user['company']
  del user['website']
  user.update({'salaryInUSD': (user["salaryInIDR"]*conv['conversion_rates']['USD'])})

with open('user.json', 'w') as json_file:
  json.dump(users, json_file)
