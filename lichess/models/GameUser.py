from pydantic import BaseModel

from .LightUser import LightUser


class GameUser(BaseModel):
    """
    GameUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameUser.yaml
    """

    user: LightUser
    rating: int
    ratingDiff: int | None = None
    name: str | None = None
    provisional: bool | None = None
    aiLevel: int | None = None
    analysis: object | None = None
    team: str | None = None
