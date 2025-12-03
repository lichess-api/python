from pydantic import BaseModel


class Profile(BaseModel):
    """
    Profile

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Profile.yaml
    """

    flag: str | None = None
    location: str | None = None
    bio: str | None = None
    realName: str | None = None
    fideRating: int | None = None
    uscfRating: int | None = None
    ecfRating: int | None = None
    cfcRating: int | None = None
    rcfRating: int | None = None
    dsbRating: int | None = None
    links: str | None = None
