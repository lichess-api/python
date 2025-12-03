from pydantic import BaseModel

from .TeamRequest import TeamRequest
from .User import User


class TeamRequestWithUser(BaseModel):
    """
    TeamRequestWithUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TeamRequestWithUser.yaml
    """

    request: TeamRequest
    user: User
