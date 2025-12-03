from typing import Literal

from pydantic import BaseModel

from .ArenaPerf import ArenaPerf
from .ArenaPosition import ArenaPosition
from .ArenaRatingObj import ArenaRatingObj
from .ArenaStatus import ArenaStatus
from .Clock import Clock
from .LightUser import LightUser
from .Variant import Variant


class MinRatedGames(BaseModel):
    nb: int


class Schedule(BaseModel):
    freq: str
    speed: str


class TeamBattle(BaseModel):
    teams: tuple[str, ...]
    nbLeaders: int


class ArenaTournament(BaseModel):
    """
    ArenaTournament

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournament.yaml
    """

    id: str
    createdBy: str
    system: Literal["arena"]
    minutes: int
    clock: Clock
    rated: bool
    fullName: str
    nbPlayers: int
    variant: Variant
    startsAt: int
    finishesAt: int
    status: ArenaStatus
    perf: ArenaPerf

    secondsToStart: int | None = None
    hasMaxRating: bool | None = None
    maxRating: ArenaRatingObj | None = None
    minRating: ArenaRatingObj | None = None
    minRatedGames: MinRatedGames | None = None
    botsAllowed: bool | None = None
    minAccountAgeInDays: int | None = None
    onlyTitled: bool | None = None
    teamMember: str | None = None
    private: bool | None = None
    position: ArenaPosition | None = None
    schedule: Schedule | None = None
    teamBattle: TeamBattle | None = None
    winner: LightUser | None = None
