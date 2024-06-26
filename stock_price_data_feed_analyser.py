# -*- coding: utf-8 -*-
"""Stock Price Data feed analyser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14m1uH8jwo7ly93IghEQhp9Z9Q2uX3nV8
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def analyze_stock_data(symbol, start_date, end_date):
    stock_data = fetch_stock_data(symbol, start_date, end_date)
    if stock_data is None:
        return
    print(stock_data.describe())
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.title(f'Stock Price Analysis for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    symbol = 'AAPL'
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    analyze_stock_data(symbol, start_date, end_date)