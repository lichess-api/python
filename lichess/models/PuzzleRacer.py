from pydantic import BaseModel, HttpUrl


class PuzzleRacer(BaseModel):
    """
    PuzzleRacer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/PuzzleRacer.yaml
    """

    id: str
    url: HttpUrl
