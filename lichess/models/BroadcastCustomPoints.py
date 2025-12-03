from pydantic import Field

BroadcastCustomPoints: float = Field(ge=0, le=10)


"""
BroadcastCustomPoints

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastCustomPoints.yaml
"""
