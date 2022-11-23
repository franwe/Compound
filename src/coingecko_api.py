import requests
from typing import List, Dict

class CoingeckoAPI:
    def __init__(self):
        self.url = "https://api.coingecko.com/api/v3"
        self.coins_endpoint = "coins"
    
    def get_coins_list(self) -> List[Dict]:
        url = f"{self.url}/{self.coins_endpoint}/list"
        params = {}

        r = requests.get(url = url, params = params)
        data = r.json()
        if "error" in data:
            raise Exception(f"Could not get Coins List. - msg: {data}")
        return data

    def get_historical_info(self, symbol: str, date: str, localization: str = "false") -> Dict:
        # date: "dd-mm-yyyy"
        url = url = f"{self.url}/{self.coins_endpoint}/{symbol}/history"
        params = {"date": date, "localization": localization}

        r = requests.get(url = url, params = params)
        data = r.json()
        if "error" in data:
            raise Exception(f"Could not get price: {symbol} {date} - msg: {data}")
        return data

    def get_historical_price_usd(self, symbol: str, date: str) -> float:
        # date: "dd-mm-yyyy"
        historical_info = self.get_historical_info(symbol, date)
        price = historical_info["market_data"]["current_price"]["usd"]
        return float(price)


if __name__ == "__main__":
    cg = CoingeckoAPI()
    coins = cg.get_coins_list()
    print([c["id"] for c in coins])

    price = cg.get_historical_price_usd("augur", "19-11-2022")
    print(price)
