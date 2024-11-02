# %% Librerias
import pandas
import pandas_ta as ta
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('bmh')

aapl = yf.download('AAPL', '2023-01-01', '2024-10-31')


# %% Medias Moviles

aapl['SMA'] = ta.sma(aapl['Close'], length=20)

aapl['EMA'] = ta.ema(aapl['Close'], length=20)



# Plot

aapl[['Close', 'SMA', 'EMA']].plot(figsize=(10, 6))
plt.show()
