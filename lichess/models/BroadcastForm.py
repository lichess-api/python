from pydantic import BaseModel, HttpUrl

from .BroadcastTiebreakExtendedCode import BroadcastTiebreakExtendedCode


class BroadcastFormInfo(BaseModel):
    format: str
    location: str
    tc: str
    fideTc: str
    timeZone: str
    players: str
    website: HttpUrl
    standings: HttpUrl


class BroadcastForm(BaseModel):
    """
    BroadcastForm

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastForm.yaml
    """

    name: str
    info: BroadcastFormInfo | None = None
    markdown: str | None = None
    showScores: bool | None = None
    showRatingDiffs: bool | None = None
    teamTable: bool | None = None
    visibility: str
    players: str
    teams: str
    tier: int
    tiebreaks: tuple[BroadcastTiebreakExtendedCode, ...]
