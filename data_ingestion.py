import yfinance as yf
import pandas as pd
meta = yf.Ticker("META")
# print(meta)

# getting META financial information
print(meta.info) 

# getting META financial metrics 
print('Company Sector: ', meta.info['sector'])
# stock price / earning per share (eps), how much investors are paying per dollar of earning 
print('P/E Ratio: ', meta.info['trailingPE'])       
print('Company Beta: ', meta.info['beta'])

# getting META information in key-value pairs
for key, value in meta.info.items():
    print(f'{key}: {value}')

# to get the historical data 
data = meta.history(period='max')
print(data.dtypes)
print(data.to_string())

# getting all the rows of META historical data
pd.set_option('display.max_rows', None)
print(data.to_string())

# getting historical data for specified period
import datetime
start_date = datetime.datetime(2019, 5, 31)
end_date = datetime.datetime(2021, 1, 30)

data = meta.history(start=start_date, end=end_date)
print("Historical Data")
print(data.to_string())
print(data.columns.tolist())

# visualize data and display in tabular format
import matplotlib.pyplot as plt
data = meta.history(period='1y')
print(data.to_string())
data['Open'].plot(title='Meta Stock Price (Last 1 year)')
plt.xlabel('Date')
plt.ylabel('Open Price (USD)')
plt.show()