from pydantic import BaseModel

from .GameColor import GameColor
from .GameSource import GameSource
from .GameStatus import GameStatus
from .Variant import Variant
from .Speed import Speed
from .GameEventOpponent import GameEventOpponent
from .GameCompat import GameCompat


class GameEventInfo(BaseModel):
    """
    GameEventInfo

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameEventInfo.yaml
    """

    fullId: str
    gameId: str
    fen: str | None = None
    color: GameColor | None = None
    lastMove: str | None = None
    source: GameSource | None = None
    status: GameStatus | None = None
    variant: Variant | None = None
    speed: Speed | None = None
    perf: str | None = None
    rated: bool | None = None
    hasMoved: bool | None = None
    opponent: GameEventOpponent | None = None
    isMyTurn: bool | None = None
    secondsLeft: int | None = None
    winner: GameColor | None = None
    ratingDiff: int | None = None
    compat: GameCompat | None = None
    id: str | None = None
