import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

df = pd.read_csv('data/sample_data.csv', index_col='Date', parse_dates=True)

plt.figure(figsize=(16, 8))
plt.title('Close Price')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price', fontsize=18)

plt.figure(figsize=(16, 8))
plt.title('Volume')
plt.plot(df['Volume'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Volume', fontsize=18)
plt.show()

df['Close Change'] = df['Adj Close'].pct_change()
df['Volume Change'] = df['Volume'].pct_change()

plt.figure(figsize=(16, 8))
plt.title('Close Daily % Change')
plt.plot(df['Close Change'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Daily % Change', fontsize=18)
plt.show()

plt.figure(figsize=(16, 8))
plt.title('Volume Daily % Change')
plt.plot(df['Volume Change'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Daily % Change', fontsize=18)
plt.show()


correlation = df['Close Change'].corr(df['Volume Change'])
print('Correlation between Adj Close Change and Volume Change:', correlation)
