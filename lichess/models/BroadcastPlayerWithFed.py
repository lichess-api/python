from pydantic import BaseModel

from .Title import Title


class BroadcastPlayerWithFed(BaseModel):
    """
    BroadcastPlayerWithFed

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastPlayerWithFed.yaml
    """

    name: str
    title: Title
    rating: int
    fideId: int
    team: str
    fed: str
