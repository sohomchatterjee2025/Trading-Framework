import matplotlib.pyplot as plt

def plot_equity(eq):
    plt.figure(figsize=(10,5))
    plt.plot(eq)
    plt.title("Equity Curve")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.grid()
    plt.show()
