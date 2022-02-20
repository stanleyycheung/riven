from collections import Counter
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

def get_most_played_champions(matches: List[Match], summoner: Summoner) -> dict:
    champion_count = Counter(match.info.participants[summoner.puuid].championName for match in matches)
    return champion_count

def get_win_rate(matches: List[Match], summoner: Summoner) -> float:
    win_loss = Counter(match.info.participants[summoner.puuid].win for match in matches)
    return win_loss[True]/sum(win_loss.values())

def get_most_played_with(summoner: Summoner, other_summoners: List[Summoner], get_win_rate: bool=True):
    aram_matches = get_aram_matches(summoner)
    played_with = {summoner.name: 0 for summoner in other_summoners}
    won_games = {summoner.name: 0 for summoner in other_summoners}
    for match in aram_matches:
        for summoner in other_summoners:
            try:
                p_info = match.get_participant_info(summoner)
                played_with[summoner.name] += 1
                if p_info.win:
                    won_games[summoner.name] += 1
            except KeyError:
                continue
    if get_win_rate:
        for summoner in won_games:
            won_games[summoner] = won_games[summoner]/played_with[summoner]
        dicts = [played_with, won_games]
        combined = {}
        for k in played_with.keys():
            combined[k] = tuple(d[k] for d in dicts)
        return dict(sorted(combined.items(), key=lambda item: item[1][1], reverse=True))
    else:
        return played_with


