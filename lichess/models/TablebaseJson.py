from typing import Literal

from pydantic import BaseModel

from .Move import Move


class TablebaseJson(BaseModel):
    """
    TablebaseJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TablebaseJson.yaml
    """

    category: Literal[
        "win",
        "unknown",
        "syzygy-win",
        "maybe-win",
        "cursed-win",
        "draw",
        "blessed-loss",
        "maybe-loss",
        "syzygy-loss",
        "loss",
    ]
    """`cursed-win` and `blessed-loss` means the 50-move rule prevents
    the decisive result.

    `syzygy-win` and `syzygy-loss` means exact result is unknown due to
    [DTZ rounding](https://syzygy-tables.info/metrics#dtz), i.e., the
    win or loss could also be prevented by the 50-move rule if
    the user has deviated from the tablebase recommendation since the
    last pawn move or capture.

    `maybe-win` and `maybe-loss` means the result with regard to the
    50-move rule is unknown because the DTC tablebase does not
    guarantee to reach a zeroing move as soon as possible.
    """
    dtz: int | None
    "[DTZ50'' with rounding](https://syzygy-tables.info/metrics#dtz) or null if unknown"
    precise_dtz: int | None
    "DTZ50'' (only if guaranteed to be not rounded) or null if unknown"
    dtc: int | None
    "Depth to Conversion (experimental)"
    dtm: int | None
    "Depth To Mate (only for Standard positions with not more than 5 pieces)"
    dtw: int | None
    "Depth To Win (only for Antichess positions with not more than 4 pieces)"
    checkmate: bool
    stalemate: bool
    variant_win: bool | None = None
    "Only in chess variants"
    variant_loss: bool | None = None
    "Only in chess variants"
    insufficient_material: bool
    moves: tuple[Move, ...]
    "Information about legal moves, best first"
