import requests
from typing import List, Dict

class TheGraphAPI:
    def __init__(self):
        self.url = "https://api.thegraph.com/subgraphs/name/graphprotocol"
        self.compound_endpoint = "compound-v2"

    def get_compound_borrows(self) -> List[Dict]:
        url = f"{self.url}/{self.compound_endpoint}"
        query = """{
                    markets {
                        underlyingSymbol
                        underlyingName
                        collateralFactor
                        exchangeRate
                        totalBorrows
                        totalSupply
                        underlyingPriceUSD
                        blockTimestamp
                    }
                    }
                """
        r = requests.post(url, json={'query': query})
        data = r.json()
        if "errors" in data:
            raise Exception(f"Could not get Compound Borrows from The Graph. - msg: {data['errors']}")
        return data["data"]["markets"]

          
if __name__ == "__main__":
    tg = TheGraphAPI()
    data = tg.get_compound_borrows()
    print(data)
