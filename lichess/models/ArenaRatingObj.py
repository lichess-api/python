from pydantic import BaseModel

from .PerfType import PerfType


class ArenaRatingObj(BaseModel):
    """
    ArenaRatingObj

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaRatingObj.yaml
    """

    perf: PerfType | None = None
    rating: int
