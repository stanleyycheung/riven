import json
import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any, List

from models.summoner import Summoner
from models.match import Match

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

GET_USER_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
GET_USER_MATCHES_URL = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
GET_MATCH_URL = "https://europe.api.riotgames.com/lol/match/v5/matches/"


def get_summoner(summoner_name: str) -> Summoner:
    url = GET_USER_URL + summoner_name + f"?api_key={API_KEY}"
    print(f'Calling: {url}')
    response = requests.get(url).json()
    try:
        summoner = Summoner(**response)
        return summoner
    except TypeError:
        print('something fucked up')
    return None


def get_recent_matches(summoner: Summoner, count: int = 20, start: int = 0) -> List[str]:
    url = f"{GET_USER_MATCHES_URL}{summoner.puuid}/ids?start={start}&count={count}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()


def get_match(match_id: str) -> Dict[str, Any]:
    url = f"{GET_MATCH_URL}{match_id}?api_key={API_KEY}"
    response = requests.get(url).json()
    try:
        match = Match(**response)
        return match
    except TypeError as e:
        print(f'fcked up {e}')
        raise
    return None
