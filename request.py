import json
import requests
import typing
import os
from typing import Dict, Any, List

from models.summoner import Summoner

API_KEY = os.getenv("RIOT_API_KEY")

get_user_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"


def get_summoner(summoner_name: str) -> Dict[str, Any]:
    url = get_user_url + summoner_name + f"?api_key={API_KEY}"
    response = requests.get(url).json()
    summoner = Summoner(**response)
    return summoner


