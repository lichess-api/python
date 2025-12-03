from pydantic import BaseModel

from .Perfs import Perfs
from .Title import Title
from .Flair import Flair
from .Profile import Profile
from .PlayTime import PlayTime
from .PatronColor import PatronColor


class User(BaseModel):
    """
    User

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/User.yaml
    """

    id: str
    username: str
    perfs: Perfs | None = None
    title: Title | None = None
    flair: Flair | None = None
    createdAt: int | None = None
    disabled: bool | None = None
    tosViolation: bool | None = None
    profile: Profile | None = None
    seenAt: int | None = None
    playTime: PlayTime | None = None
    patron: bool | None = None
    patronColor: PatronColor | None = None
    verified: bool | None = None
