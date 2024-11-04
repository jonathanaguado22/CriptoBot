# %% Librerías
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import yfinance as yf

plt.style.use('bmh')

# Descargar datos
appl = "AAPL"
appl_data = yf.download(appl, start="2023-01-01", end="2023-12-31")

# Verifica los primeros datos descargados
print("Primeras filas de los datos descargados:")
print(appl_data.head())

if isinstance(appl_data.columns, pd.MultiIndex):
    appl_data.columns = appl_data.columns.get_level_values(0)
# %% Medias Móviles

appl_data['SMA'] = ta.sma(appl_data['Close'], length=50)
appl_data['EMA'] = ta.ema(appl_data['Close'], length=50)

# Mostrar las primeras y últimas filas de SMA y EMA calculadas

print(appl_data[['Close', 'SMA', 'EMA']].head(10))


print(appl_data[['Close', 'SMA', 'EMA']].dropna().tail())

# %% Plot
# Graficar los datos de cierre, SMA y EMA
appl_data[['Close', 'SMA', 'EMA']].plot(figsize=(10, 6))
plt.legend()
plt.show()

#%% Bandas de Bolinger
if isinstance(appl_data.columns, pd.MultiIndex):
    appl_data.columns = appl_data.columns.get_level_values(0)
# %% Calcular Bandas de Bollinger

bbands = ta.bbands(appl_data['Close'], length=20)

appl_data['upper_band'] = bbands['BBU_20_2.0']
appl_data['middle_band'] = bbands['BBM_20_2.0']
appl_data['lower_band'] = bbands['BBL_20_2.0']

# Mostrar los datos de Bandas de Bollinger calculadas
print(appl_data[['Close', 'upper_band', 'middle_band', 'lower_band']].head(10))
print(appl_data[['Close', 'upper_band', 'middle_band', 'lower_band']].dropna().tail())

appl_data[['Close', 'upper_band','middle_band','lower_band' ]].plot(figsize=(15, 15))
plt.show()