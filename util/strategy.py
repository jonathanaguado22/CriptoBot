import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import yfinance as yf


class Strategy:

    def __init__(self, data):

        self.close = data.get("Close")
        self.open = data.get("Open")
        self.high = data.get("High")

        