from pydantic import BaseModel


class GameEventOpponent(BaseModel):
    """
    GameEventOpponent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameEventOpponent.yaml
    """

    id: str
    username: str
    rating: int
    ratingDiff: int | None = None
