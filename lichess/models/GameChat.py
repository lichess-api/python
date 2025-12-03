from pydantic import BaseModel


class GameChatMessage(BaseModel):
    text: str
    user: str


type GameChat = tuple[GameChatMessage, ...] | tuple[GameChatMessage]

"""
GameChat

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameChat.yaml
"""
