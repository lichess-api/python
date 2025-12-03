from pydantic import BaseModel


class BroadcastGroupTour(BaseModel):
    """
    BroadcastGroupTour

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastGroupTour.yaml
    """

    id: str
    name: str
    active: bool
    live: bool
