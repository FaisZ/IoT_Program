import pandas as pd
import time
import matplotlib.pyplot as plt

file_path = 'logs/sensor_log.json'


fig, axs = plt.subplots(4)
fig.suptitle('Temperature')
axs[0].set_ylabel('Min')
axs[1].set_ylabel('Max')
axs[2].set_ylabel('Mean')
axs[3].set_ylabel('Median')

#main program loop
while True:
  try:
    #read and normalize log file
    sensor = pd.read_json(file_path)
    res = pd.json_normalize(sensor["array"])

    #aggregate data and group by roomArea
    res = res.groupby(['roomArea']).agg(['min','max','mean','median'])
    print(res)
    axs[0].bar(res.index,res["temperature"]["min"])
    axs[1].bar(res.index,res["temperature"]["max"])
    axs[2].bar(res.index,res["temperature"]["mean"])
    axs[3].bar(res.index,res["temperature"]["median"])
    plt.pause(3)

    #show the average of all sensors
    print("All sensors average")
    print(res.agg(['min','max','mean','median']))

    #to simulate 15 minute streams
    time.sleep(2)
    
  #Stop when ctrl+c pressed
  except KeyboardInterrupt:
    print("Program stopped.")
    break

  #retrying of exception found
  except:
    print("Error occured. Retrying...")
    continue
