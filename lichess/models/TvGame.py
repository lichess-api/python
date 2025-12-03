from pydantic import BaseModel

from .LightUser import LightUser
from .GameColor import GameColor


class TvGame(BaseModel):
    """
    TvGame

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TvGame.yaml
    """

    user: LightUser
    rating: int
    gameId: str
    color: GameColor
