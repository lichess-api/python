from pydantic import BaseModel

from .PerfTop10 import PerfTop10


class Top10s(BaseModel):
    """
    Top10s

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Top10s.yaml
    """

    bullet: PerfTop10
    blitz: PerfTop10
    rapid: PerfTop10
    classical: PerfTop10
    ultraBullet: PerfTop10
    crazyhouse: PerfTop10
    chess960: PerfTop10
    kingOfTheHill: PerfTop10
    threeCheck: PerfTop10
    antichess: PerfTop10
    atomic: PerfTop10
    horde: PerfTop10
    racingKings: PerfTop10
