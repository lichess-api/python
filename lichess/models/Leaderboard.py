from pydantic import BaseModel

from .TopUser import TopUser


class Leaderboard(BaseModel):
    """
    Leaderboard

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Leaderboard.yaml
    """

    users: tuple[TopUser, ...]
