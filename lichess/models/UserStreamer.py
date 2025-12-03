from pydantic import BaseModel, HttpUrl, Field


class Twitch(BaseModel):
    channel: HttpUrl


class Youtube(BaseModel):
    channel: HttpUrl


class UserStreamer(BaseModel):
    """
    UserStreamer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserStreamer.yaml
    """

    twitch: Twitch
    youtube: Youtube = Field(alias="youTube")
