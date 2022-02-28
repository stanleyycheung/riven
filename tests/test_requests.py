
from unittest.mock import patch
from riven.request import call_url, get_recent_matches, get_summoner
from mocks import SUMMONER_MOCK_RESPONSE, MOCK_SUMMONER


class TestRequest:

    @patch('riven.request.requests.get')
    def test_call_url(self, mock_get):
        mock_get.return_value = SUMMONER_MOCK_RESPONSE
        api_call = call_url('test_url')
        assert api_call == SUMMONER_MOCK_RESPONSE

    @patch('riven.request.call_url')
    def test_get_summoner(self, mock_call_url):
        mock_call_url.return_value.json.return_value = SUMMONER_MOCK_RESPONSE
        summoner = get_summoner('test_summoner')
        assert summoner.summoner_id == SUMMONER_MOCK_RESPONSE['id']
        assert summoner.accountId == SUMMONER_MOCK_RESPONSE['accountId']
        assert summoner.puuid == SUMMONER_MOCK_RESPONSE['puuid']
        assert summoner.name == SUMMONER_MOCK_RESPONSE['name']
        assert summoner.profileIconId == SUMMONER_MOCK_RESPONSE['profileIconId']
        assert summoner.summonerLevel == SUMMONER_MOCK_RESPONSE['summonerLevel']

    @patch('riven.request.call_url')
    def test_get_no_summoner(self, mock_call_url):
        mock_call_url.return_value.json.return_value = {}
        mock_call_url.status_code = 200
        summoner = get_summoner('test_summoner')

    @patch('riven.request.call_url')
    def test_get_recent_matches(self, mock_call_url):
        mock_call_url.return_value.json.return_value = []
        recent_matches = get_recent_matches(MOCK_SUMMONER, 0, 100)

    def test_get_match(self):
        pass
