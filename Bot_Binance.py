# Bot para el mercado de criptomoneda con Binance
from pprint import pprint
from binance.spot import Spot
from numpy import integer
from sqlalchemy import INTEGER

import config


class BotBinance:

     __api_key = config.API_KEY
     __api_secret = config.API_SECRET

     def __init__(self, pair: str, temporality: str):

         self.pair = pair.upper()
         self.temporality = temporality
         self.symbol = self.pair.removesuffix("USDT")

     def binance_spot(self):

         return Spot(self.__api_key, self.__api_secret)

     def balances_positive(self) -> list[dict]:

         return [ cryptos for cryptos in self.binance_spot().account()['balances'] if float(cryptos['free']) > 0]


bot = BotBinance("btcusdt", "6h")
price_bitcoin = bot.binance_spot().ticker_price("BTCUSDT")['price']
bitcoin = float(price_bitcoin)
pprint(bitcoin)




