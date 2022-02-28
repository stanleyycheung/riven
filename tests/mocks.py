from riven.models.summoner import Summoner


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
