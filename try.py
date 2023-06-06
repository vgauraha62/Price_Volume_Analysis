from typing import Any

import yfinance as yf
import matplotlib.pyplot as plt
import mplcyberpunk
from statistics import mean
import pandas as pd
import numpy as np
import os
import seaborn as sns

from sklearn.metrics import confusion_matrix

# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

symbol = "SBIN.NS"
# symbol = input() + ".NS"
data1 = yf.download(tickers=symbol, period="1y", interval="1d", ignore_tz=True, prepost=False)
print(data1.head(10))

x = data1['Open']
y = data1['Close']
A = data1['Adj Close']
Y = y - x
V = data1['Volume']
# print(V.head(10))

# Load a sample dataset
# df = pd.read_csv('data/sample_data.csv')

# # Calculate the correlation matrix
# corr_matrix = df[['Volume', 'Adj Close']].corr()
#
# # Display the correlation matrix as a heatmap
# plt.matshow(corr_matrix)
# plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
# plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
# plt.colorbar()
# plt.show()


# # Load the data from a CSV file
# df = pd.read_csv('data/sample_data.csv')
#
# # Define the true labels and predicted labels
# y_true = df['Adj Close']
# y_pred = df['Close']
#
# # Compute the confusion matrix
# cm = confusion_matrix(y_true, y_pred)
#
# # Display the confusion matrix as a heatmap
# sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
# plt.xlabel('Adj Close')
# plt.ylabel('Close')
# plt.show()


# Create a folder to store the CSV file (if it doesn't exist)
folder_name = 'data'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save the DataFrame as a CSV file in the specified folder
file_name = os.path.join(folder_name, 'sample_data.csv')
data1.to_csv(file_name, index=True)

# print(V.head())

plt.style.use("cyberpunk")
plt.plot(Y)
mplcyberpunk.add_gradient_fill()
plt.show()

plt.style.use("cyberpunk")
plt.plot(V)
mplcyberpunk.add_glow_effects()
plt.show()

U1 = V[1]
U2 = V[2]
U3 = V[3]
U4 = V[4]
U5 = V[5]


# V_cell_1 = V.iat[10, 1]


# print(V_cell_1)
# print(U1,U2,U3,U4,U5)


def Analysis(Y, A, analysis):
    return analysis


# if y>x:
#    print("strength")
# else:

#    print("weakness")




# Add a legend to the plot
#ax.legend()

# Show the plot
#plt.show()
