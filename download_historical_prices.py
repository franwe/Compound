import pandas as pd
from pathlib import Path
from typing import Dict
import json
import time

from coingecko_api import CoingeckoAPI

CONFIGS_DIR = Path.cwd().joinpath("configs")
OUT_FILE = Path.cwd().joinpath("data", "coingecko_prices.csv")


def download(asset: str, date: str) -> Dict:
    date_str = date.strftime("%d-%m-%Y")
    cg_api.get_historical_price_usd(asset["id"], date_str)
    line_dict = {
        "date": date.date(), 
        "symbol": asset["symbol"], 
        "id": asset["id"], 
        "price": cg_api.get_historical_price_usd(asset["id"], date_str)
        }
    return line_dict


def load_empty_line(asset: str, date: str) -> Dict:
    return {
        "date": date.date(), 
        "symbol": asset["symbol"], 
        "id": asset["id"], 
        "price": None
        }


if __name__ == "__main__":
    
    # setup
    dates = pd.date_range(start="2022-10-21", end="2022-11-21", freq="1D")
    with open(CONFIGS_DIR.joinpath("coingecko_assets.json")) as f:
        assets = json.load(f)
    cg_api = CoingeckoAPI()

    print(f"Script will run for more than {len(assets)*len(dates)*6/60} minutes. \
        ({len(assets)*len(dates)} requests with 6 sec sleep)")

    # download loop
    for date in dates:
        for asset in assets.values():
            try: 
                line_dict = download(asset, date)
            except Exception as e:
                print(f" --- failed to download . try again - {asset} {date}")
                try:
                    time.sleep(30)
                    line_dict = download(asset, date)
                except Exception as e:
                    print(f" --- failed to download again ! save empty - {asset} {date}")
                    line_dict = load_empty_line(asset, date)

            print(line_dict)
            line = pd.DataFrame(line_dict, index=[0])
            if not OUT_FILE.exists():
                line.to_csv(OUT_FILE, index=False)
            else:
                line.to_csv(OUT_FILE, mode='a', index=False, header=False)
            time.sleep(6)
