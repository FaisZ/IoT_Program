import pandas as pd
import time

file_path = 'logs/sensor_log.json'

#main program loop
while True:
  try:

    sensor = pd.read_json(file_path)

    res = pd.json_normalize(sensor["array"])
    print(res.groupby(['roomArea']).agg(['min','max','mean','median']))
    print("All sensors average")
    print(res.agg(['min','max','mean','median']))
    time.sleep(4)

#average sensors value
#loop every 15 minutes

  #Stop when ctrl+c pressed
  except KeyboardInterrupt:
    print("Program stopped.")
    break

  #retrying of exception found
  except:
    print("Error occured. Retrying...")
    continue
