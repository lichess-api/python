from pydantic import BaseModel


class ArenaTournamentPlayer(BaseModel):
    """
    ArenaTournamentPlayer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournamentPlayer.yaml
    """

    games: int
    score: int
    rank: int
    performance: int | None = None
