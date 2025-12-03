from pydantic import BaseModel


class GameCompat(BaseModel):
    """
    GameCompat

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameCompat.yaml
    """

    bot: bool
    board: bool
