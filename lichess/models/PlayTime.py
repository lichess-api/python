from pydantic import BaseModel


class PlayTime(BaseModel):
    """
    Play time

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/PlayTime.yaml
    """

    total: int
    tv: int
