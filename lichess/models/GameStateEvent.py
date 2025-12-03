from typing import Literal

from pydantic import BaseModel

from .GameStatusName import GameStatusName
from .GameColor import GameColor


class GameStateEvent(BaseModel):
    """
    GameState event

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStateEvent.yaml
    """

    type: Literal["gameState"]
    moves: str
    "Current moves in UCI format (King to rook for Chess690-compatible castling notation)"
    wtime: int
    "Integer of milliseconds White has left on the clock"
    btime: int
    "Integer of milliseconds Black has left on the clock"
    winc: int
    "Integer of White Fisher increment."
    binc: int
    "Integer of Black Fisher increment."
    status: GameStatusName
    winner: GameColor | None = None
    "Color of the winner, if any"
    wdraw: bool | None = None
    bdraw: bool | None = None
    wtakeback: bool | None = None
    btakeback: bool | None = None
