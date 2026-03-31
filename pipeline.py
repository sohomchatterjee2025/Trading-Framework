from config import CONFIG
from src.data_loader import DataLoader
from src.factors import FactorEngine
from src.model import SignalModel
from src.backtester import Backtester
from src.metrics import Metrics
from src.utils import plot_equity
import numpy as np

# Load data
data = DataLoader(CONFIG["ticker"], CONFIG["period"]).load()

# Build factors
fe = FactorEngine()
factors = fe.build(data)

# Target
returns = data['Close'].pct_change().shift(-1)
target = (returns > 0).astype(int)

factors = factors.loc[target.index].dropna()
target = target.loc[factors.index]

# Train model
model = SignalModel()
model.train(factors, target)

# Predict signals
signals = model.predict(factors)
signals = np.where(signals == 1, 1, -1)

# Backtest
bt = Backtester(data['Close'].loc[factors.index], signals, CONFIG["initial_capital"])
rets, equity = bt.run()

# Metrics
print("Sharpe:", Metrics.sharpe(rets))
print("Max Drawdown:", Metrics.max_drawdown(rets))
print("Win Rate:", Metrics.win_rate(rets))

# Plot
plot_equity(equity)
