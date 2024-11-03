# %% Librerias
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('bmh')

# Descargar datos
aapl = yf.download('AAPL', '2019-01-01', '2021-05-03')
aapl.dropna(inplace=True)
# Verifica los primeros datos descargados
print(aapl.head())

# %% Medias Moviles
aapl['SMA'] = ta.sma(aapl['Close'], 50 )
aapl['EMA'] = ta.ema(aapl['Close'], 50)

# Verifica los primeros datos con SMA y EMA calculados
print(aapl[['Close', 'SMA', 'EMA']].head())
print(aapl.head())
# Plot
aapl[['Close', 'SMA', 'EMA']].plot(figsize=(10, 6))
plt.show()
