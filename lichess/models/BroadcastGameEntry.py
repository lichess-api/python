from pydantic import BaseModel

from .BroadcastPlayerWithFed import BroadcastPlayerWithFed
from .GameColor import GameColor
from .BroadcastCustomPoints import BroadcastCustomPoints


class BroadcastGameEntry(BaseModel):
    """
    BroadcastGameEntry

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastGameEntry.yaml
    """

    round: str
    "ID of the round"
    id: str
    opponent: BroadcastPlayerWithFed
    color: GameColor
    points: str | None = None
    customPoints: float | None = BroadcastCustomPoints
    ratingDiff: int | None = None
