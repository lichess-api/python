from pydantic import BaseModel

from .Flair import Flair
from .Title import Title
from .PatronColor import PatronColor


class LightUser(BaseModel):
    """
    LightUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/LightUser.yaml
    """

    id: str
    name: str
    flair: Flair | None = None
    title: Title | None = None
    patron: bool | None = None
    patronColor: PatronColor | None = None
