from typing import Literal

from pydantic import BaseModel


class OpponentGoneEvent(BaseModel):
    """
    OpponentGoneEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/OpponentGoneEvent.yaml
    """

    type: Literal["opponentGone"]
    gone: bool
    claimWinInSeconds: int | None = None
