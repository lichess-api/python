from pydantic import BaseModel

from .BroadcastRoundInfo import BroadcastRoundInfo
from .BroadcastTour import BroadcastTour
from .BroadcastRoundStudyInfo import BroadcastRoundStudyInfo


class BroadcastMyRound(BaseModel):
    """
    BroadcastMyRound

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastMyRound.yaml
    """

    round: BroadcastRoundInfo
    tour: BroadcastTour
    study: BroadcastRoundStudyInfo
