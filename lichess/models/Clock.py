from pydantic import BaseModel


class Clock(BaseModel):
    """
    Clock

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Clock.yaml
    """

    limit: int
    increment: int
