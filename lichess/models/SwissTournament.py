from pydantic import BaseModel

from .SwissStatus import SwissStatus
from .Verdicts import Verdicts


class SwissTournament(BaseModel):
    """
    SwissTournament

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/SwissTournament.yaml
    """

    id: str
    createdBy: str
    startsAt: str
    name: str
    clock: object
    variant: str
    round: int
    nbRounds: int
    nbPlayers: int
    nbOngoing: int
    status: SwissStatus
    stats: object
    rated: bool
    verdicts: Verdicts
    nextRound: object | None = None
