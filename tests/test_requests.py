
from unittest.mock import patch
from riven.request import get_summoner
from mock_responses import SUMMONER_MOCK_RESPONSE


class TestRequest:
    @patch('riven.request.call_url')
    def test_get_summoner(self, mock_call_url):
        mock_call_url.return_value.json.return_value = SUMMONER_MOCK_RESPONSE
        test_summoner = get_summoner('test_summoner')
        assert test_summoner.summoner_id == SUMMONER_MOCK_RESPONSE['id']
        assert test_summoner.accountId == SUMMONER_MOCK_RESPONSE['accountId']
        assert test_summoner.puuid == SUMMONER_MOCK_RESPONSE['puuid']
        assert test_summoner.name == SUMMONER_MOCK_RESPONSE['name']
        assert test_summoner.profileIconId == SUMMONER_MOCK_RESPONSE['profileIconId']
        assert test_summoner.summonerLevel == SUMMONER_MOCK_RESPONSE['summonerLevel']

    def get_recent_matches(self):
        pass
