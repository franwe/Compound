import requests
import time


class CompoundApi:
    def __init__(self):
        self.url = "https://api.compound.finance/api/v2/"
        self.accounts_endpoint = "account"

    def _get_accounts(self, amount:int=10, page:int=1, min_borrow_value_in_eth:float=0.0, max_health:float=10.0):
        url = f"{self.url}/{self.accounts_endpoint}/?page_number={page}&page_size={amount}&max_health[value]={max_health}&min_borrow_value_in_eth[value]={min_borrow_value_in_eth}"
        params = {}

        r = requests.get(url = url, params = params)
        data = r.json()
        if "errors" in data or (("error" in data) and (data["error"])):
            raise Exception(f"Could not get Coins List. - msg: {data}")
        return data

    def get_accounts(self, amount:int=10, min_borrow_value_in_eth:float=0.0, max_health:float=10.0):
        # uses _get_accounts() to request batches of max 200 accounts
        request_max_n = 200
        accounts = []
        remaining_n = amount
        page = 1
        while remaining_n > 0:
            n = min(remaining_n, request_max_n)
            acc = self._get_accounts(n, page, min_borrow_value_in_eth, max_health)
            accounts += acc["accounts"]
            if len(acc["accounts"]) < n:
                accounts += acc["accounts"]
                print(f"Request only found {len(accounts)} accounts, asked {amount}.")
            remaining_n -= request_max_n
            page += 1
            time.sleep(5)
        return accounts


if __name__ == "__main__":
    c_api = CompoundApi()
    print(c_api.get_accounts(amount=10, min_borrow_value_in_eth=0.002, max_health=2.0))
