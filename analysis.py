from typing import List
from models.match import Match
from models.summoner import Summoner
import request


def get_aram_matches(summoner: Summoner, num_of_matches = 500) -> List[Match]:
    match_ids = request.get_recent_matches(summoner, num_of_matches)
    matches = []
    for match_id in match_ids:
        match = request.get_match(match_id)
        if match.get_game_mode() == 'ARAM':
            matches.append(match)
    return matches


    