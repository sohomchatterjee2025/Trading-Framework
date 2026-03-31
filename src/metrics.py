import numpy as np

class Metrics:

    @staticmethod
    def sharpe(r):
        return np.mean(r) / np.std(r)

    @staticmethod
    def max_drawdown(r):
        cum = (1 + r).cumprod()
        peak = cum.cummax()
        dd = (cum - peak) / peak
        return dd.min()

    @staticmethod
    def win_rate(r):
        return (r > 0).mean()
