import requests
import pandas as pd


class Api(object):
    def __init__(self):
        self.REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
        self.APP_ID = '1060146276538691344'

        self.params = {
            "applicationId": self.APP_ID,
            "format": "json",
            "keyword": "4901730077002",  # 商品名をキーワードにすると関係ないものもヒットしまくるので、JANコードで指定 #バンドエイド
            "availability": 1,  # 販売可能な商品がどうか 「1」は販売可能
            "hits": 30,  # 1ページあたりの取得件数 1から30までの整数で
            "sort": "+itemPrice"  # 価格順（昇順）で
        }

    def call_api(self):
        self.res = requests.get(self.REQUEST_URL, self.params)
        self.result = self.res.json()
        items = self.result['Items']
        items_info = []
        for i, item in enumerate(items):
            item_info = []
            item_info.append((item['Item']['itemName']))
            item_info.append((item['Item']['itemPrice']))
            items_info.append(item_info)
        print(items_info)

    def __del__(self):
        pass


if __name__ == '__main__':
    api = Api()
    api.call_api()
    del api
