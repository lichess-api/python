from pydantic import BaseModel, Field

from .LightUser import LightUser


class UserNote(BaseModel):
    """
    UserNote

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserNote.yaml
    """

    from_: LightUser = Field(alias="from")
    to: LightUser
    text: str
    date: int
