import requests
import os
from typing import Dict, Any, List
from models.summoner import Summoner
from limiter import rate_limiter

API_KEY = os.getenv("RIOT_API_KEY")

get_user_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
get_user_matches_url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
get_match_url = "https://europe.api.riotgames.com/lol/match/v5/matches/"


class APIRequestException(Exception):
    """Error when making API call"""

@rate_limiter
def call_url(url):
    print(f'Calling: {url}')
    return requests.get(url)

def get_summoner(summoner_name: str) -> Summoner:
    url = get_user_url + summoner_name + f"?api_key={API_KEY}"
    response = call_url(url)
    if response:
        summoner = Summoner(**response.json())
    else:
        raise APIRequestException(f'Error {response.status_code} when making {url} call')
    return summoner


def get_recent_matches(summoner: Summoner, count: int = 20, start: int = 0) -> List[str]:
    url = f"{get_user_matches_url}{summoner.puuid}/ids?start={start}&count={count}&api_key={API_KEY}"
    response = call_url(url)
    return response.json()


def get_match(match_id: str) -> Dict[str, Any]:
    url = f"{get_match_url}{match_id}?api_key={API_KEY}"
    response = call_url(url)
    return response.json()
