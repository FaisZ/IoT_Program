import pandas as pd
import json
import os
import time
import random
from pathlib import Path

file_path = 'logs/sensor_log.json'

data = []
myFile = Path(file_path)

#if file not exist or file empty
if myFile.is_file() == False or os.stat(file_path).st_size == 0:
  os.makedirs('logs', exist_ok=True)

  #initialize a new dictionary to be put in the log file
  data = {}
  data["array"] = []
  with open(file_path,'w+') as logFile:
    json.dump(data, logFile)

#main program loop
while True:
  try:
    data = []
    #append the log file with new data
    with open(file_path,"r+") as logFile:
      data = json.load(logFile)

      #data generation
      liveStream = {
        'temperature': random.randint(0,100),
        'humidity': random.randint(0,100),
        'roomArea': 'room'+str(random.randint(1,10))
      }
      data["array"].append(liveStream)
      print(liveStream)

    #to write to json file the newly generated data
    with open(file_path,'w+') as logFile:
      json.dump(data, logFile)
    
    #sleep to simulate 2 minutes push rate
    time.sleep(120)

  #Stop when ctrl+c pressed
  except KeyboardInterrupt:
    print("Program stopped.")
    break

  #retrying if exception found
  except Exception as e:
    print("Error occured."+str(e))
    print("Retrying in 5 seconds...")
    time.sleep(5)
    continue
