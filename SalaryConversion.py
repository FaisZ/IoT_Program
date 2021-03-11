import json
import urllib.request
import pandas as pd
from currency_converter import CurrencyConverter
from endpoints import Controller

#to stream from endpoints
class Default(Controller):
  def GET(self):
    return main()

def main():
  #source data for users
  with urllib.request.urlopen('http://jsonplaceholder.typicode.com/users') as userUrl:
      users = pd.read_json(userUrl.read().decode())

  #source data for conversion rates
  with urllib.request.urlopen('https://v6.exchangerate-api.com/v6/af83cf7542205b242e8041b8/latest/IDR') as conversion:
      conv = json.loads(conversion.read().decode())

  #source data for user salary
  with open('JSON/salary_data.json') as s:
    sal = pd.read_json(s)

  #the resulting array after normalizing the json
  salary = pd.json_normalize(sal["array"])

  #merging users with their salary based on id
  res = pd.merge(users, salary, left_on='id', right_on='id', how='left').drop(['company','website'], axis=1)

  #calculating salary in usd
  res["salaryInUSD"] = res["salaryInIDR"]*conv['conversion_rates']['USD']
  return res.to_json()
