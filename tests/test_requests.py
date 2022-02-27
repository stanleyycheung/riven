
from unittest.mock import patch

from riven.request import get_summoner


class TestRequest:

    @patch('riven.request.call_url')
    def test_get_summoner(self, mock_call_url):
        mock_response ={
            "id": "test_id",
            "accountId": "test_accountId",
            "puuid": "test_puuid",
            "name": "test_summoner",
            "profileIconId": 0,
            "revisionDate": 0,
            "summonerLevel": 0
        }
        mock_call_url.return_value.json.return_value = mock_response
        test_summoner = get_summoner('test_summoner')
        assert test_summoner.summoner_id == mock_response['id']
        assert test_summoner.accountId == mock_response['accountId']
        assert test_summoner.puuid == mock_response['puuid']
        assert test_summoner.name == mock_response['name']
        assert test_summoner.profileIconId == mock_response['profileIconId']
        assert test_summoner.summonerLevel == mock_response['summonerLevel']


