from pydantic import BaseModel


class RP(BaseModel):
    before: int
    after: int


class UserActivityScore(BaseModel):
    """
    UserActivityScore

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserActivityScore.yaml
    """

    win: int
    loss: int
    draw: int
    rp: RP
