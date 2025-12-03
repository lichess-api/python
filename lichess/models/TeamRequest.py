from pydantic import BaseModel


class TeamRequest(BaseModel):
    """
    TeamRequest

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TeamRequest.yaml
    """

    teamId: str
    userId: str
    date: int
    message: str | None = None
