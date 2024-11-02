# %% Librerias

import talib
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('bmh')

aapl = yf.download('AAPL', '2023-01-01', '2024-10-31')


# %% Medias Moviles

aapl['SMA'] = tab.SMA(aapl['Close'].values, timeperiod=21)
aapl['EMA'] = tab.EMA(aapl['Close'].values, timeperiod=55)


# Plot

aapl[['Close', 'SMA', 'EMA']].plot(figsize=(10, 6))
