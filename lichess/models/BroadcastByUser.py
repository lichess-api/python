from pydantic import BaseModel

from .BroadcastTour import BroadcastTour


class BroadcastByUser(BaseModel):
    """
    BroadcastByUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastByUser.yaml
    """

    tour: BroadcastTour
