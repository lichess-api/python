from pydantic import BaseModel

from .Perf import Perf
from .PuzzleModePerf import PuzzleModePerf


class Perfs(BaseModel):
    """
    Performances

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Perfs.yaml
    """

    chess960: Perf
    atomic: Perf
    racingKings: Perf
    ultraBullet: Perf
    blitz: Perf
    kingOfTheHill: Perf
    threeCheck: Perf
    antichess: Perf
    crazyhouse: Perf
    bullet: Perf
    correspondence: Perf
    horde: Perf
    puzzle: Perf
    classical: Perf
    rapid: Perf
    storm: PuzzleModePerf
    racer: PuzzleModePerf
    streak: PuzzleModePerf
