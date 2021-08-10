import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google and Apple!

""")

tickerSymbol1 = 'GOOGL'
tickerSymbol2 = 'AAPL'
todayDate = datetime.today().strftime('%Y-%m-%d')
tickerData1 = yf.Ticker(tickerSymbol1)
tickerData2 = yf.Ticker(tickerSymbol2)
tickerDf1 = tickerData1.history(period='1d', start='2010-5-31', end=todayDate)
tickerDf2 = tickerData2.history(period='1d', start='2010-5-31', end=todayDate)
st.write("""
## Google
""")
st.write("""
### Closing Price
""")
st.line_chart(tickerDf1.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf1.Volume)
st.write("""
## Apple
""")
st.write("""
### Closing Price
""")
st.line_chart(tickerDf2.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf2.Volume)