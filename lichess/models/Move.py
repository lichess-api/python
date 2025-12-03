from typing import Literal

from pydantic import BaseModel


class Move(BaseModel):
    """
    Move

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Move.yaml
    """

    uci: str
    san: str
    category: Literal[
        "loss",
        "unknown",
        "syzygy-loss",
        "maybe-loss",
        "blessed-loss",
        "draw",
        "cursed-win",
        "maybe-win",
        "syzygy-win",
        "win",
    ]
    dtz: int | None
    "DTZ50'' with rounding or null if unknown"
    precise_dtz: int | None
    "DTZ50'' (only if guaranteed to be not rounded) or null if unknown"
    dtc: int | None
    "Depth to Conversion (experimental)"
    dtm: int | None
    "Depth To Mate (only for Standard positions with not more than 5 pieces)"
    dtw: int | None
    "Depth To Win (only for Antichess positions with not more than 4 pieces)"
    zeroing: bool
    checkmate: bool
    stalemate: bool
    variant_win: bool
    variant_loss: bool
    insufficient_material: bool
