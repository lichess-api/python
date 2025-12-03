from pydantic import BaseModel

from .Title import Title


class TopUser(BaseModel):
    """
    TopUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TopUser.yaml
    """

    id: str
    username: str
    perfs: object | None = None
    title: Title | None = None
    patron: bool | None = None
    online: bool | None = None
