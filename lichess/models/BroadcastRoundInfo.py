from pydantic import BaseModel, HttpUrl

from .BroadcastCustomScoring import BroadcastCustomScoring


class BroadcastRoundInfo(BaseModel):
    """
    BroadcastRoundInfo

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastRoundInfo.yaml
    """

    id: str
    name: str
    slug: str
    createdAt: int
    rated: bool
    "Whether the round is used for rating calculations"
    ongoing: bool | None = None
    startsAt: int | None = None
    startsAfterPrevious: bool | None = None
    """The start date/time is unknown and the round will start automatically
    when the previous round completes"""
    finishedAt: int | None = None
    finished: bool | None = None
    url: HttpUrl
    delay: int | None = None
    customScoring: BroadcastCustomScoring | None = None
