from typing import Literal

from pydantic import BaseModel

from .GameEventInfo import GameEventInfo


class GameStartEvent(BaseModel):
    """
    GameStartEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStartEvent.yaml
    """

    type: Literal["gameStart"]
    game: GameEventInfo
