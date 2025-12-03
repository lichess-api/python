from pydantic import BaseModel

from .BroadcastTour import BroadcastTour
from .BroadcastRoundInfo import BroadcastRoundInfo


class BroadcastWithLastRound(BaseModel):
    """
    BroadcastWithLastRound

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastWithLastRound.yaml
    """

    group: str
    tour: BroadcastTour
    round: BroadcastRoundInfo
