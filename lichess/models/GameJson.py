from pydantic import BaseModel

from .VariantKey import VariantKey
from .Speed import Speed
from .GameStatusName import GameStatusName
from .GameUsers import GameUsers
from .GameColor import GameColor
from .GameMoveAnalysis import GameMoveAnalysis


class GameJson(BaseModel):
    """
    GameJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameJson.yaml
    """

    id: str
    rated: bool
    variant: VariantKey
    speed: Speed
    perf: str
    createdAt: int
    lastMoveAt: int
    status: GameStatusName
    players: GameUsers

    source: str | None = None
    initialFen: str | None = None
    winner: GameColor | None = None
    opening: object | None = None
    moves: str | None = None
    pgn: str | None = None
    daysPerTurn: int | None = None
    analysis: tuple[GameMoveAnalysis, ...] | None = None
    tournament: str | None = None
    swiss: str | None = None
    clock: object | None = None
    clocks: tuple[int, ...] | None = None
    division: object | None = None
