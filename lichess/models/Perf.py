from pydantic import BaseModel


class Perf(BaseModel):
    """
    Performance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Perf.yaml
    """

    games: int
    rating: int
    rd: int
    prog: int
    prov: bool | None = None
