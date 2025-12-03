from pydantic import BaseModel


class Crosstable(BaseModel):
    """
    Crosstable

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Crosstable.yaml
    """

    users: dict[str, float]
    nbGames: int
