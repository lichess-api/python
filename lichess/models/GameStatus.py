from pydantic import BaseModel

from .GameStatusId import GameStatusId
from .GameStatusName import GameStatusName


class GameStatus(BaseModel):
    """
    GameStatus

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStatus.yaml
    """

    id: GameStatusId
    name: GameStatusName
