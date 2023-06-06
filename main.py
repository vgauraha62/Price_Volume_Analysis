import yfinance as yf
import pandas as pd


msft = yf.Ticker("MSFT")
tcs = yf.Ticker("TCS")
sbi = yf.Ticker("SBI")

#df = sbi.info
# print(df)
# print(tcs.info)

df = sbi.history(period="1mo")
print(df)
# show meta information about the history (requires history() to be called first)
# msft.history_metadata
