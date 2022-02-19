from typing import Dict, List, Any


class Match:

    def __init__(self, metadata: Dict[str, Any], info: Dict[str, Any]):
        self.metadata = MetadataDto(**metadata)
        self.info = InfoDto(info)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} @ [{self.metadata}], [{self.info}]'


class MetadataDto:

    def __init__(self, dataVersion: str, matchId: str, participants: List[str]):

        self.dataVersion = dataVersion
        self.matchId = matchId
        self.participants = participants

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} @ {self.matchId}'


class InfoDto:

    def __init__(self, info: Dict[str, Any]):
        self.gameMode: str = info['gameMode']
        self.gameType: str = info['gameType']

        self.mapId = info['mapId']

        self.participants = [ParticipantDto(
            participant) for participant in info['participants']]
        self.teams = [TeamDto(team) for team in info['teams']]

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} @ {self.gameMode}, {self.gameType}'


class ParticipantDto:

    def __init__(self, participantInfo: Dict[str, Any]):
        self.assists: int = participantInfo['assists']
        self.championName: str = participantInfo['championName']
        self.championId: int = participantInfo['championId']
        self.deaths: int = participantInfo['deaths']
        self.goldEarned: int = participantInfo['goldEarned']
        self.kills: int = participantInfo['kills']
        self.participantId: int = participantInfo['participantId']
        self.timeCCingOthers: int = participantInfo['timeCCingOthers']
        self.totalDamageDealtToChampions: int = participantInfo['totalDamageDealtToChampions']
        self.win: bool = participantInfo['win']

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} @ {self.participantId}'


class TeamDto:

    def __init__(self, teamInfo: Dict[str, Any]):
        self.kills: int = teamInfo['objectives']['champion']['kills']
        self.teamId: int = teamInfo['teamId']
        self.win: bool = teamInfo['win']

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} @ {self.teamId}'
