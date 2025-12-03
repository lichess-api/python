from typing import Literal


type UciVariant = Literal[
    "chess", "crazyhouse", "antichess", "atomic", "horde", "kingofthehill", "racingkings", "3check"
]

"""
UciVariant

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UciVariant.yaml
"""
