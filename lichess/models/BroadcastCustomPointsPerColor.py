from pydantic import BaseModel


from .BroadcastCustomPoints import BroadcastCustomPoints


class BroadcastCustomPointsPerColor(BaseModel):
    """
    BroadcastCustomPointsPerColor

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastCustomPointsPerColor.yaml
    """

    win: float = BroadcastCustomPoints
    draw: float = BroadcastCustomPoints
