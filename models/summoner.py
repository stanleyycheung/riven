

class Summoner:
    def __init__(self,
                 accountId: str,
                 profileIconId: str,
                 revisionDate: str,
                 name: str,
                 id: str,
                 puuid: str,
                 summonerLevel: str) -> None:
        self.accountId = accountId
        self.profileIconId = profileIconId
        self.revisionDate = revisionDate
        self.name = name
        self.summoner_id = id
        self.puuid = puuid
        self.summonerLevel = summonerLevel

    def __repr__(self) -> str:
        return f'{self.name} @ {self.puuid}'
