from matplotlib import pyplot as plt

def plot_mc_paths(symbol, mc):
    fig, ax = plt.subplots(1,1)
    for p in mc:
        ax.plot(p)

    ax.set_xlabel("Days")
    ax.set_ylabel("Price [USD]")
    fig.suptitle(f"Simulated Price Paths - {symbol}")
    return fig


def plot_returns_histogram(returns, N, bins=50):
    fig = plt.hist(returns, bins=bins)
    plt.xlabel("Returns")
    plt.ylabel("Amount")
    plt.title(f"Simulated Portfolio Returns (N={N})")
    return fig
