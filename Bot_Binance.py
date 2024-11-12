# Bot para el mercado de criptomoneda con Binance
from pprint import pprint
from binance.spot import Spot
from numpy import integer
from sqlalchemy import INTEGER

import config


class BotBinance:

     __api_key = config.API_KEY
     __api_secret = config.API_SECRET
     binance_client = Spot(api_key = __api_key, api_secret = __api_secret)

     def __init__(self, pair: str, temporality: str):

         self.pair = pair.upper()
         self.temporality = temporality
         self.symbol = self.pair.removesuffix("USDT")

     def request(self, endpoint: str, params: dict = None):
      try:
       response = getattr(self.binance_client, endpoint)
       return response() if params is None else response(**params)
      except Exception as e:
          pass

     def balances_positive(self) -> list[dict]:

         return [ cryptos for cryptos in self.binance_spot().account()['balances'] if float(cryptos['free']) > 0]




bot = BotBinance("btcusdt", "6h")
price_bitcoin = bot.binance_spot().ticker_price("BTCUSDT")['price']
bitcoin = float(price_bitcoin)
pprint(bot.binance_spot())




