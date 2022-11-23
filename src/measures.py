from typing import List
import numpy as np


def calc_volatility(p: np.array) -> float:
    log_returns = np.log(p[1:]/p[:-1])
    return np.std(log_returns)


def simulate_path(start_price: float, volatility: float, horizon: int) -> np.array:
    # TODO: check formula
    returns = np.random.normal(loc=0, scale=volatility, size=horizon)
    returns = np.hstack([np.zeros(1), returns])  # add return=0 for starting day
    t = np.tril(np.ones(len(returns+1)))
    v = np.dot(t, returns)
    s = np.exp(v) * start_price
    return s


def monte_carlo_simulation(start_price: float, volatility: float, horizon: int, paths: int) -> np.array:
    paths = [simulate_path(start_price, volatility, horizon)[-1] for _ in range(paths)]
    return np.array(paths)


def calc_value_usd(n_ctoken, exchange_rate, prices):
    # create shapes
    s = n_ctoken.reshape((n_ctoken.shape[0], 1))
    x = exchange_rate.reshape((exchange_rate.shape[0], 1))
    if len(prices.shape) == 1:
        p = prices.reshape((prices.shape[0], 1))
    else:
        p = prices

    # multiply element-wise 
    values = np.multiply(s * x, p)
    return values


def calc_borrow_value_usd(n_ctoken, exchange_rate, prices):
    return calc_value_usd(n_ctoken, exchange_rate, prices)


def calc_collateral_value_usd(n_ctoken, exchange_rate, collateral_factor, prices):
    f = collateral_factor.reshape((n_ctoken.shape[0], 1))
    values = calc_value_usd(n_ctoken, exchange_rate, prices)
    return np.multiply(f, values)
