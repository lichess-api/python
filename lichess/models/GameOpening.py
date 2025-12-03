from pydantic import BaseModel


class GameOpening(BaseModel):
    """
    GameOpening

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameOpening.yaml
    """

    eco: str
    name: str
    ply: int
