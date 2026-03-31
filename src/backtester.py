import numpy as np
import pandas as pd

class Backtester:

    def __init__(self, prices, signals, capital):
        self.prices = prices
        self.signals = signals
        self.capital = capital

    def run(self):
        returns = self.prices.pct_change().fillna(0)

        positions = self.signals.shift(1).fillna(0)
        strat_returns = returns * positions

        equity = (1 + strat_returns).cumprod() * self.capital

        return strat_returns, equity
