from pydantic import BaseModel

from .ArenaTournament import ArenaTournament
from .ArenaTournamentPlayer import ArenaTournamentPlayer


class ArenaTournamentPlayed(BaseModel):
    """
    ArenaTournamentPlayed

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournamentPlayed.yaml
    """

    tournament: ArenaTournament
    player: ArenaTournamentPlayer
