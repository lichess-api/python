from pydantic import BaseModel

from .VariantKey import VariantKey
from .Clock import Clock


class BulkPairingGame(BaseModel):
    id: str
    black: str
    white: str


class BulkPairing(BaseModel):
    """
    BulkPairing

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BulkPairing.yaml
    """

    id: str
    games: tuple[BulkPairingGame, BulkPairingGame]
    variant: VariantKey
    clock: Clock
    pairAt: int
    pairedAt: int | None
    rated: bool
    startClocksAt: int
    scheduledAt: int
