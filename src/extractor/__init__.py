import requests
import json
import time


class ExtractData:
    def __init__(self):
        self.QUANTITY = 1000
        self.DATA_LIMIT = 10000
        self.URL = f"https://fakerapi.it/api/v1/persons?_quantity={self.QUANTITY}&_birthday_start=1900-01-01"

    def extract_data(self):
        try:
            data = []
            tries = 0
            max_retries = 3
            while len(data) < self.DATA_LIMIT:
                response = requests.get(self.URL)
                if response.status_code != 200:
                    print('Failed to get data from API, waiting for retry', {"status_code": response.status_code})
                    time.sleep(30)
                    if tries >= max_retries:
                        break
                    tries +=1
                    continue
                _data = json.loads(response.text)
                for _row in _data["data"]:
                    data.append(_row)
            print("Data retrieved from API", {"lenght": len(data)})
            return data
        except Exception as err:
            print("Failed to get data from API", {"error": err})
