from typing import Literal

from pydantic import BaseModel

from .Variant import Variant
from .Speed import Speed
from .GameEventPlayer import GameEventPlayer
from .GameStateEvent import GameStateEvent


class GameFullEventClock(BaseModel):
    initial: int
    "Initial time in milliseconds"
    increment: int
    "Increment time in milliseconds"


class GameFullEventPerf(BaseModel):
    name: str
    'Translated perf name (e.g. "Classical" or "Blitz")'


class GameFullEvent(BaseModel):
    """
    GameFullEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameFullEvent.yaml
    """

    type: Literal["gameFull"]
    id: str
    variant: Variant
    clock: GameFullEventClock
    speed: Speed
    perf: object
    rated: bool
    createdAt: int
    white: GameEventPlayer
    black: GameEventPlayer
    initialFen: str
    state: GameStateEvent
    daysPerTurn: int | None = None
    tournamentId: str | None = None
