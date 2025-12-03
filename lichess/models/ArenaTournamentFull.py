from pydantic import BaseModel, HttpUrl

from .Title import Title
from .PatronColor import PatronColor
from .Flair import Flair
from .Clock import Clock
from .ArenaSheet import ArenaSheet
from .Verdicts import Verdicts
from .ArenaRatingObj import ArenaRatingObj


class Spotlight(BaseModel):
    headline: str


class Quote(BaseModel):
    text: str
    author: str


class GreatPlayer(BaseModel):
    name: str
    url: HttpUrl


class MinRatedGames(BaseModel):
    nb: int


class Perf(BaseModel):
    icon: str
    key: str
    name: str


class Schedule(BaseModel):
    freq: str
    speed: str


class DuelPlayer(BaseModel):
    n: str
    r: int
    k: int


class Duel(BaseModel):
    id: str
    p: tuple[DuelPlayer, DuelPlayer]


class StandingPlayer(BaseModel):
    name: str
    title: Title
    patron: bool
    patronColor: PatronColor
    flair: Flair
    rank: int
    rating: int
    score: int
    sheet: ArenaSheet


class Standing(BaseModel):
    page: int
    players: tuple[StandingPlayer, ...]


class FeaturedPlayer(BaseModel):
    name: str
    id: str
    rank: int
    rating: int


class FeaturedClock(BaseModel):
    white: int
    "white's clock in seconds"
    black: int
    "black's clock in seconds"


class Featured(BaseModel):
    id: str
    fen: str
    orientation: str
    color: str
    lastMove: str
    white: FeaturedPlayer
    black: FeaturedPlayer
    c: FeaturedClock


class PodiumElementNumbers(BaseModel):
    game: int
    berserk: int
    win: int


class PodiumElement(BaseModel):
    name: str
    title: Title
    patron: bool
    patronColor: PatronColor
    flair: Flair
    rank: int
    rating: int
    score: int
    nb: PodiumElementNumbers
    performance: int


class Stats(BaseModel):
    games: int
    moves: int
    whiteWins: int
    blackWins: int
    draws: int
    berserks: int
    averageRating: int


class ArenaTournamentFull(BaseModel):
    """
    ArenaTournamentFull

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournamentFull.yaml
    """

    id: str
    fullName: str
    rated: bool | None = None
    spotlight: Spotlight | None = None
    berserkable: bool | None = None
    onlyTitled: bool | None = None
    clock: Clock
    minutes: int | None = None
    createdBy: str | None = None
    system: str | None = None
    secondsToStart: int | None = None
    secondsToFinish: int | None = None
    isFinished: bool | None = None
    isRecentlyFinished: bool | None = None
    pairingsClosed: bool | None = None
    startsAt: str | None = None
    nbPlayers: int
    verdicts: Verdicts | None = None
    quote: Quote | None = None
    "The quote displayed on the tournament page"
    greatPlayer: GreatPlayer | None = None
    allowList: tuple[str, ...] | None = None
    "List of usernames allowed to join the tournament"
    hasMaxRating: bool | None = None
    maxRating: ArenaRatingObj | None = None
    minRating: ArenaRatingObj | None = None
    minRatedGames: MinRatedGames | None = None
    botsAllowed: bool | None = None
    minAccountAgeInDays: int | None = None
    perf: Perf | None = None
    schedule: Schedule | None = None
    description: str | None = None
    variant: str | None = None
    duels: Duel | None = None
    standing: Standing | None = None
    featured: Featured | None = None
    podium: tuple[PodiumElement, ...] | None = None
    stats: Stats | None = None
    myUsername: str | None = None
