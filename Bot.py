# %% Librerias

import talib as ta
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('bmh')

aapl = yf.download('AAPL', '2024-01-01', '2024-10-31')