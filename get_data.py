import requests as req
import numpy as np
import pandas as pd

get_data = req.get('http://api.bitcoincharts.com/v1/markets.json')

data_content = get_data.content

df = pd.io.json.read_json(data_content)

#remove inactive exchanges (check volume column)
df = df[(df.volume != 0)]

#sort by price
sorted_df = df.sort(['avg'],ascending=[1])

#reindex dataframe
sorted_df = sorted_df.reset_index()

if __name__ == '__main__':

    print(sorted_df)
                                                                  
