from pydantic import BaseModel

from .PerfType import PerfType


class ArenaPerf(BaseModel):
    """
    Arena performance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaPerf.yaml
    """

    key: PerfType
    name: str
    position: int
    icon: str | None = None
