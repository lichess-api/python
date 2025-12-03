from pydantic import BaseModel

from .GameUser import GameUser


class GameUsers(BaseModel):
    """
    GameUsers

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameUsers.yaml
    """

    white: GameUser
    black: GameUser
