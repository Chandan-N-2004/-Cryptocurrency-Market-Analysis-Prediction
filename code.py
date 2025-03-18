import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf

# Load stock dataset (Assuming CSV file with 'Date', 'Open', 'High', 'Low', 'Close', 'Volume')
data = pd.read_csv("stock_data.csv", parse_dates=["Date"], index_col="Date")

# Calculate daily returns
data["Daily Return"] = data["Close"].pct_change()

# Moving Averages (50-day & 200-day)
data["SMA_50"] = data["Close"].rolling(window=50).mean()
data["SMA_200"] = data["Close"].rolling(window=200).mean()

# Bollinger Bands
rolling_std = data["Close"].rolling(window=20).std()
data["Upper Band"] = data["SMA_50"] + (rolling_std * 2)
data["Lower Band"] = data["SMA_50"] - (rolling_std * 2)

# Volatility Calculation
data["Volatility"] = data["Daily Return"].rolling(window=20).std()

# Plot stock price trends with moving averages
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Close"], label="Closing Price", color="blue")
plt.plot(data.index, data["SMA_50"], label="50-day SMA", linestyle="dashed", color="red")
plt.plot(data.index, data["SMA_200"], label="200-day SMA", linestyle="dotted", color="green")
plt.fill_between(data.index, data["Upper Band"], data["Lower Band"], color='gray', alpha=0.3, label='Bollinger Bands')
plt.title("Stock Price Trends with Moving Averages & Bollinger Bands")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# Daily Returns Histogram
sns.histplot(data["Daily Return"].dropna(), bins=50, kde=True, color="purple")
plt.title("Daily Return Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.show()

# Volatility Plot
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Volatility"], label="20-day Rolling Volatility", color="orange")
plt.title("Stock Volatility Over Time")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.show()

# Candlestick Chart
mpf.plot(data, type='candle', volume=True, style='charles', title='Stock Candlestick Chart')

# Display summary statistics
print(data.describe())
