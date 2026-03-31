import pandas as pd
import numpy as np

class FactorEngine:

    def momentum(self, df, w=10):
        return df['Close'].pct_change(w)

    def mean_reversion(self, df, w=5):
        return -df['Close'].pct_change(w)

    def volatility(self, df, w=20):
        return df['Close'].pct_change().rolling(w).std()

    def rsi(self, df, w=14):
        delta = df['Close'].diff()
        gain = delta.clip(lower=0).rolling(w).mean()
        loss = (-delta.clip(upper=0)).rolling(w).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def build(self, df):
        factors = pd.DataFrame(index=df.index)

        factors['momentum'] = self.momentum(df)
        factors['mean_rev'] = self.mean_reversion(df)
        factors['volatility'] = self.volatility(df)
        factors['rsi'] = self.rsi(df)

        return factors.dropna()
