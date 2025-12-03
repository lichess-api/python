from pydantic import BaseModel

from .BroadcastWithLastRound import BroadcastWithLastRound


class BroadcastTopPast(BaseModel):
    currentPage: int
    maxPerPage: int
    currentPageResults: tuple[BroadcastWithLastRound, ...]
    previousPage: int | None
    nextPage: int | None


class BroadcastTop(BaseModel):
    """
    BroadcastTop

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastTop.yaml
    """

    active: tuple[BroadcastWithLastRound, ...]
    upcoming: tuple[BroadcastWithLastRound, ...]
    past: BroadcastTopPast
