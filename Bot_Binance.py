# Bot para el mercado de criptomoneda con Binance

from binance.spot import Spot
import config

client = Spot(api_key= config.API_KEY,
              api_secret= config.API_SECRET)


