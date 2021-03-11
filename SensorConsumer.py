import pandas as pd
import time

file_path = 'logs/sensor_log.json'

#main program loop
while True:
  try:
    #read and normalize log file
    sensor = pd.read_json(file_path)
    res = pd.json_normalize(sensor["array"])

    #aggregate data and group by roomArea
    print(res.groupby(['roomArea']).agg(['min','max','mean','median']))

    #show the average of all sensors
    print("All sensors average")
    print(res.agg(['min','max','mean','median']))

    #to simulate 15 minute streams
    time.sleep(900)
    
  #Stop when ctrl+c pressed
  except KeyboardInterrupt:
    print("Program stopped.")
    break

  #retrying of exception found
  except:
    print("Error occured. Retrying...")
    continue
