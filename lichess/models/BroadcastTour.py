from typing import Literal

from pydantic import BaseModel, HttpUrl

from .LightUser import LightUser


class BroadcastTourInfo(BaseModel):
    "Additional display information about the tournament"

    website: HttpUrl
    "Official website. External website URL"
    players: str
    "Featured players"
    location: str
    "Tournament location"
    tc: str
    "Time control"
    fideTc: Literal["standard", "rapid", "blitz"]
    "FIDE rating category"
    timeZone: str
    """Timezone of the tournament. Example: `America/New_York`.
    See [list of possible timezone identifiers](
    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for more.
    """
    standings: HttpUrl
    "Official standings website. External website URL"
    format: str
    "Tournament format"


class BroadcastTour(BaseModel):
    """
    BroadcastTour

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastTour.yaml
    """

    id: str
    name: str
    slug: str
    createdAt: int
    dates: tuple[int, int] | None = None
    "Start and end dates of the tournament, as Unix timestamps in milliseconds"
    info: BroadcastTourInfo | None = None
    "Additional display information about the tournament"
    tier: int | None = None
    "Used to designate featured tournaments on Lichess"
    image: HttpUrl | None = None
    description: str | None = None
    "Full tournament description in markdown format, or in HTML if the html=1 query parameter is set."
    leaderboard: bool | None = None
    teamTable: bool | None = None
    url: HttpUrl
    communityOwner: LightUser | None = None
