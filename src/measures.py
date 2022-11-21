from typing import List
import numpy as np


def calc_volatility(p: np.array) -> float:
    log_returns = np.log(p[1:]/p[:-1])
    return np.std(log_returns)


def simulate_path(start_price: float, volatility: float, horizon: int) -> np.array:
    # TODO: check formula
    returns = np.random.normal(loc=0, scale=volatility, size=horizon)
    t = np.tril(np.ones(len(returns)))
    v = np.dot(t, returns)
    s = np.exp(v) * start_price
    return s


def monte_carlo_simulation(start_price: float, volatility: float, horizon: int, paths: int) -> np.array:
    paths = [simulate_path(start_price, volatility, horizon) for _ in range(paths)]
    return np.array(paths)
