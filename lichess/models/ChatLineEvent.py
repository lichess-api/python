from typing import Literal

from pydantic import BaseModel


class ChatLineEvent(BaseModel):
    """
    ChatLineEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChatLineEvent.yaml
    """

    type: Literal["chatLine"]
    room: Literal["player", "spectator"]
    username: str
    text: str
