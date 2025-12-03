from pydantic import BaseModel

from .BroadcastCustomPointsPerColor import BroadcastCustomPointsPerColor


class BroadcastCustomScoring(BaseModel):
    """
    BroadcastCustomScoring

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastCustomScoring.yaml
    """

    white: BroadcastCustomPointsPerColor
    black: BroadcastCustomPointsPerColor
