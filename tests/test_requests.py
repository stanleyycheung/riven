
import json
import os
import re
from unittest.mock import MagicMock, patch

from riven.models.match import InfoDto, MetadataDto
from riven.models.summoner import Summoner
from riven.request import APIRequestException, call_url, get_match, get_recent_matches, get_summoner

MOCK_MATCH_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'matches')

SUMMONER_MOCK_RESPONSE = {
    "id": "test_id",
    "accountId": "test_accountId",
    "puuid": "test_puuid",
    "name": "test_summoner",
    "profileIconId": 0,
    "revisionDate": 0,
    "summonerLevel": 0
}

MOCK_SUMMONER = Summoner(**SUMMONER_MOCK_RESPONSE)


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
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.__bool__.return_value = False
        mock_call_url.return_value = mock_response
        try:
            get_summoner('test_summoner')
        except APIRequestException as e:
            assert str(mock_response.status_code) in str(e)

    @patch('riven.request.call_url')
    def test_get_recent_matches(self, mock_call_url):

        def mock_matches(url):
            print(url)
            try:
                start = int(re.search(r'start=(\d+)&', url).group(1))
                count = int(re.search(r'count=(\d+)&', url).group(1))
            except AttributeError as e:
                raise Exception(f'Url called has no start and/or count: {url}') from e
            mock_response = MagicMock()
            mock_response.json.return_value = [i for i in range(start, start+count) if i < match_limit]
            return mock_response
        match_limit = 1000
        mock_call_url.side_effect = mock_matches
        recent_matches = get_recent_matches(MOCK_SUMMONER, 50)
        assert len(recent_matches) == 50
        recent_matches = get_recent_matches(MOCK_SUMMONER, 150, start=200)
        assert len(recent_matches) == 150
        recent_matches = get_recent_matches(MOCK_SUMMONER, match_limit*2)
        assert len(recent_matches) == match_limit

    @patch('riven.request.call_url')
    def test_get_match(self, mock_call_url):
        mock_match = os.path.join(MOCK_MATCH_DIR, 'match_EUW1_5756305812.json')
        with open(mock_match, 'r') as json_file:
            json_data = json_file.read()
        json_dict = json.loads(json_data)
        mock_call_url.return_value.json.return_value = json_dict
        match = get_match('EUW1_5756305812')
        assert match
