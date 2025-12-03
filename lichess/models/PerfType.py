from typing import Literal


type PerfType = Literal[
    "ultraBullet",
    "bullet",
    "blitz",
    "rapid",
    "classical",
    "correspondence",
    "chess960",
    "crazyhouse",
    "antichess",
    "atomic",
    "horde",
    "kingOfTheHill",
    "racingKings",
    "threeCheck",
]

"""
PerfType

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/PerfType.yaml
"""
