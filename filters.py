from models.summoner import Summoner
from models.match import Match


def is_gameType(match: Match, gameType: str) -> bool:
    return match.info.gameType == gameType


def is_gameMode(match: Match, gameMode: str) -> bool:
    return match.info.gameMode == gameMode
