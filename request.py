import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any, List

from models.summoner import Summoner
from models.match import Match
from limiter import rate_limiter

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

GET_USER_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
GET_USER_MATCHES_URL = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
GET_MATCH_URL = "https://europe.api.riotgames.com/lol/match/v5/matches/"


class APIRequestException(Exception):
    """Error when making API call"""


@rate_limiter
def call_url(url):
    print(f'Calling: {url}')
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


def get_recent_matches(summoner: Summoner, count: int = 20, start: int = 0) -> List[str]:
    url = f"{GET_USER_MATCHES_URL}{summoner.puuid}/ids?start={start}&count={count}&api_key={API_KEY}"
    response = call_url(url)
    return response.json()


def get_match(match_id: str) -> Match:
    url = f"{GET_MATCH_URL}{match_id}?api_key={API_KEY}"
    response = call_url(url)
    if response:
        match = Match(**response.json())
    else:
        raise APIRequestException(
            f'Error {response.status_code} when making {url} call')
    return match
