import pandas as pd
import requests
import datetime



symbol = 'LTCUSDT'
interval = '1h'
limit = 100 #1000 Max
coin = 1

# Initialize an empty list to store data
data_list = []

url_klines = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
kline_response = requests.get(url_klines)
kline_data = kline_response.json()
for kline_item in kline_data:
    timestamp = int(kline_item[0])
    dt_object = datetime.datetime.fromtimestamp(timestamp / 1000)
    new_data = {
        'Date': dt_object,
        'Symbol': symbol,
        'Open': kline_item[1],
        'High': kline_item[2],
        'Low': kline_item[3],
        'Close': kline_item[4],
        'Volume': kline_item[5]
    }
    data_list.append(new_data)

# Create a DataFrame from the list of dictionaries
all_data = pd.DataFrame(data_list)

# Save the DataFrame to a CSV file
all_data.to_csv(f'{symbol}candle_data.csv', index=False)

