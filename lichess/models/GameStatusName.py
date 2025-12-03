from typing import Literal


type GameStatusName = Literal[
    "created",
    "started",
    "aborted",
    "mate",
    "resign",
    "stalemate",
    "timeout",
    "draw",
    "outoftime",
    "cheat",
    "noStart",
    "unknownFinish",
    "insufficientMaterialClaim",
    "variantEnd",
]

"""
GameStatusName

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStatusName.yaml
"""
