from pydantic import BaseModel

from .BroadcastGroupTour import BroadcastGroupTour


class BroadcastGroup(BaseModel):
    """
    BroadcastGroup

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastGroup.yaml
    """

    id: str
    slug: str
    name: str
    tours: tuple[BroadcastGroupTour, ...]
