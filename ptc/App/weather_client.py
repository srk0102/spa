import requests
import json

class WeatherClient:
    API_BASE_URL = 'http://samples.openweathermap.org/data/2.5/weather'
    APP_ID = 'appid=b6907d289e10d714a6e88b30761fae22'

    def __init__(self, appid = APP_ID):
        self.app_id = appid

    def get_weather_by_zip(self, zip_code):
        params = {'zip': zip_code,
                  'appid': self.app_id}
        res = requests.get(url=WeatherClient.API_BASE_URL,
                           params=params)

        if res.status_code != 200:
            raise requests.HTTPError()

        result_json = json.loads(res.content.decode())
        return result_json['weather'][0]['description']



if __name__ == '__main__':
    weather_client = WeatherClient()
    weather = weather_client.get_weather_by_zip(zip_code='60564')
    print(weather)