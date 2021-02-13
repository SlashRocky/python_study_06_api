import requests
import pandas as pd


class Api(object):
    def __init__(self):
        self.REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
        self.APP_ID = '1060146276538691344'

        self.params = {
            "applicationId": self.APP_ID,
            "format": "json",
            "genreId": "200162",  # コミック
        }

    def call_api(self):
        self.res = requests.get(self.REQUEST_URL, self.params)
        self.result = self.res.json()

    def output_to_csv(self):
        df = pd.DataFrame()
        items = self.result['Items']
        for i, item in enumerate(items):
            item_info = item['Item']

            # 扱いづらいKeyは削除
            item_info.pop('mediumImageUrls')
            item_info.pop('smallImageUrls')

            _df = pd.DataFrame(item_info, index=[i])
            df = df.append(_df)

        df[['rank', 'itemName', 'itemPrice', 'itemUrl', 'reviewAverage']].to_csv('comic.csv', index=False)

    def __del__(self):
        pass


if __name__ == '__main__':
    api = Api()
    api.call_api()
    api.output_to_csv()
    del api
