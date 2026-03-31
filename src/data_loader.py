import yfinance as yf

class DataLoader:
    def __init__(self, ticker, period):
        self.ticker = ticker
        self.period = period

    def load(self):
        df = yf.download(self.ticker, period=self.period)
        df = df[['Open','High','Low','Close','Volume']]
        df.dropna(inplace=True)
        return df
