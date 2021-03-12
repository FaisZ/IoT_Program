import pandas as pd
import time
import matplotlib.pyplot as plt

file_path = 'logs/sensor_log.json'

fig, axs = plt.subplots(2,2)
fig.suptitle('Latest Sensor Data')
axs[0,0].set_ylabel('Mean')
axs[0,0].set_title("Temperature")
axs[1,0].set_ylabel('Median')
axs[0,1].set_ylabel('Mean')
axs[0,1].set_title("Humidity")
axs[1,1].set_ylabel('Median')

#main program loop
while True:
  try:
    #read and normalize log file
    sensor = pd.read_json(file_path)
    res = pd.json_normalize(sensor["array"])

    #aggregate data and group by roomArea
    res = res.groupby(['roomArea']).agg(['min','max','mean','median'])
    print(res)
    bars1 = axs[0,0].bar(res.index,res["temperature"]["mean"], color='mediumslateblue')
    bars2 = axs[1,0].bar(res.index,res["temperature"]["median"], color='mediumslateblue')
    bars3 = axs[0,1].bar(res.index,res["humidity"]["mean"], color='lightseagreen')
    bars4 = axs[1,1].bar(res.index,res["humidity"]["median"], color='lightseagreen')

    #pause to reload after new data has been obtained
    plt.pause(400)

    #show the average of all sensors
    print("All sensors average")
    print(res.agg(['min','max','mean','median']))

    #to simulate 15 minute streams
    time.sleep(500)
    bars1.remove()
    bars2.remove()
    bars3.remove()
    bars4.remove()
    
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
