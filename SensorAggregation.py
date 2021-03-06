import pandas as pd
from endpoints import Controller

#to stream from endpoints
class Default(Controller):
  def GET(self):
    return main()

def main():
  file_path = 'JSON/sensor_data.json'
  sensor = pd.read_json(file_path)

  #the resulting array after normalizing the json
  res = pd.json_normalize(sensor["array"])

  #deleting unnecessary column
  del res['id']

  #converting timestamp to datetime, then obtain the date and replace timestamp
  res['timestamp'] = pd.to_datetime(res['timestamp'], unit='ms').dt.date

  grouped_res = res.groupby(['roomArea','timestamp']).agg(['min','max','mean','median'])
  #printing result grouped by roomArea and date
  print(grouped_res)

  return grouped_res.to_json()
