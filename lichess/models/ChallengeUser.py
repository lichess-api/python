from pydantic import BaseModel

from .Title import Title
from .Flair import Flair
from .PatronColor import PatronColor


class ChallengeUser(BaseModel):
    """
    ChallengeUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeUser.yaml
    """

    id: str
    name: str
    rating: float | None = None
    title: Title | None = None
    flair: Flair | None = None
    patron: bool | None = None
    patronColor: PatronColor | None = None
    provisional: bool | None = None
    online: bool | None = None
    lag: int | None = None
