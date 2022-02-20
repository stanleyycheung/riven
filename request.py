import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any, List
import requests_cache
from models.summoner import Summoner
from models.match import Match
from limiter import rate_limiter


load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

GET_USER_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
GET_USER_MATCHES_URL = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
GET_MATCH_URL = "https://europe.api.riotgames.com/lol/match/v5/matches/"

# install cache
requests_cache.install_cache('cache')

class APIRequestException(Exception):
    """Error when making API call"""


@rate_limiter
def call_url(url: str) -> dict:
    return requests.get(url)


def get_summoner(summoner_name: str) -> Summoner:
    url = GET_USER_URL + summoner_name + f"?api_key={API_KEY}"
    response = call_url(url)
    if response:
        summoner = Summoner(**response.json())
    else:
        raise APIRequestException(
            f'Error {response.status_code} when making {url} call')
    return summoner


def get_recent_matches(summoner: Summoner, number: int, start: int = 0) -> List[str]:
    responses = []
    count = min(100, number - start)
    url = f"{GET_USER_MATCHES_URL}{summoner.puuid}/ids?start={start}&count={count}&api_key={API_KEY}"
    responses.extend(call_url(url).json())
    while number - (start + count) > 0:
        start += count
        count = min(100, number - start)
        url = f"{GET_USER_MATCHES_URL}{summoner.puuid}/ids?start={start}&count={count}&api_key={API_KEY}"
        responses.extend(call_url(url).json())
    return responses


def get_match(match_id: str) -> Match:
    url = f"{GET_MATCH_URL}{match_id}?api_key={API_KEY}"
    response = call_url(url)
    if response:
        match = Match(**response.json())
    else:
        raise APIRequestException(
            f'Error {response.status_code} when making {url} call')
    return match
