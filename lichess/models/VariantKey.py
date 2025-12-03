from typing import Literal


type VariantKey = Literal[
    "standard",
    "chess960",
    "crazyhouse",
    "antichess",
    "atomic",
    "horde",
    "kingOfTheHill",
    "racingKings",
    "threeCheck",
    "fromPosition",
]

"""
VariantKey

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/VariantKey.yaml
"""
