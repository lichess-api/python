from pydantic import HttpUrl

from .User import User
from .Count import Count
from .UserStreamer import UserStreamer


class UserExtended(User):
    """
    UserExtended

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserExtended.yaml
    """

    url: HttpUrl
    playing: HttpUrl | None = None
    count: Count | None = None
    streaming: bool | None = None
    streamer: UserStreamer | None = None
    followable: bool | None = None
    "only appears if the request is authenticated with OAuth2"
    following: bool | None = None
    "only appears if the request is authenticated with OAuth2"
    blocking: bool | None = None
    "only appears if the request is authenticated with OAuth2"
