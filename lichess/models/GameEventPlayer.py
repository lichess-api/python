from pydantic import BaseModel

from .Title import Title


class GameEventPlayer(BaseModel):
    """
    GameEventPlayer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameEventPlayer.yaml
    """

    aiLevel: int | None = None
    id: str
    name: str
    title: Title | None
    rating: int | None = None
    provisional: bool | None = None
