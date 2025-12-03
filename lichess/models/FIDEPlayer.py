from pydantic import BaseModel

from .Title import Title


class FIDEPlayer(BaseModel):
    """
    FIDEPlayer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/FIDEPlayer.yaml
    """

    id: int
    name: str
    title: Title | None = None
    federation: str
    year: int | None = None
    inactive: int | None = None
    standard: int | None = None
    rapid: int | None = None
    blitz: int | None = None
