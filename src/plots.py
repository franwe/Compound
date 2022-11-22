from matplotlib import pyplot as plt

def plot_mc_paths(symbol, mc):
    fig, ax = plt.subplots(1,1)
    for p in mc:
        ax.plot(p)

    ax.set_xlabel("Days")
    ax.set_ylabel("Price [USD]")
    fig.suptitle(f"Simulated Price Paths - {symbol}")
    return fig
