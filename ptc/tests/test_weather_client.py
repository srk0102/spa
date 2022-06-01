import requests
from unittest import TestCase
from unittest.mock import patch

from App.weather_client import WeatherClient


class TestWeatherClient(TestCase):
    SAMPLE_RESPONSE = b"""{"coord":{"lon": -122.09,"lat": 37.39},' \
      b'"weather":[{"id": 500,"main": "Rain",' \
      b'"description":"light rain","icon": "10d"}],"base": "stations","main": {"temp": 280.44,' \
      b'"pressure":1017,"humidity": 61,"temp_min": 279.15,"temp_max": 281.15},"visibility": 12874,' \
      b'"wind":{"speed": 8.2,"deg": 340,"gust": 11.3},"clouds": {"all": 1},"dt": 1519061700,"sys": {"type": 1,' \
      b'"id": 392,"message": 0.0027,"country": "US","sunrise": 1519051894,"sunset": 1519091585},"id": 0,' \
      b'"name": "Mountain View","cod": 200)\n """

    @patch('requests.get')
    def test_Climate_by_zip_code_of_city(self, mock_requests):
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.content = TestWeatherClient.SAMPLE_RESPONSE

        weather_client = WeatherClient()
        result = weather_client.get_weather_by_zip('60564')
        print(result)
        self.assertEqual(result, 'light rain')