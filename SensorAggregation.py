import pandas as pd

sensor = pd.read_json('JSON/sensor_data.json')

res = pd.json_normalize(sensor["array"])
del res['id']
res['timestamp'] = pd.to_datetime(res['timestamp'], unit='ms').dt.date
print(res.groupby(['roomArea','timestamp']).agg(['min','max','mean','median']))
