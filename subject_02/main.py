import requests
import pandas as pd


class Api(object):
    def __init__(self):
        self.REQUEST_URL = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
        self.APP_ID = '1060146276538691344'

        self.params = {
            "applicationId": self.APP_ID,
            "format": "json",
            "keyword": "4971710464290",  # 商品名をキーワードにすると関係ないものもヒットしまくるので、JANコードで指定 # 美容液
            "hits": 30,  # 1ページあたりの取得件数 1から30までの整数で
            "sort": "-satisfied"  # 満足順（降順）で
        }

    def call_api(self):
        self.res = requests.get(self.REQUEST_URL, self.params)
        self.result = self.res.json()
        print('購入可能な最低価格：', self.result['Products'][0]['Product']['salesMinPrice'])
        print('購入可能な最低価格：', self.result['Products'][0]['Product']['salesMaxPrice'])

    def __del__(self):
        pass


if __name__ == '__main__':
    api = Api()
    api.call_api()
    del api
