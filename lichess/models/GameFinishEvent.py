from typing import Literal

from pydantic import BaseModel

from .GameEventInfo import GameEventInfo


class GameFinishEvent(BaseModel):
    """
    GameFinishEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameFinishEvent.yaml
    """

    type: Literal["gameFinish"]
    game: GameEventInfo
