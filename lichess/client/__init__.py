import logging
from typing import Literal
from collections.abc import Iterable

from pydantic import BaseModel


from .session import TokenSession, Requestor

from .formats import JSON

from ..models import (
    GameStartEvent,
    GameFinishEvent,
    ChallengeEvent,
    ChallengeCanceledEvent,
    ChallengeDeclinedEvent,
    GameFullEvent,
    GameStateEvent,
    ChatLineEvent,
    OpponentGoneEvent,
)


type ApiStreamEvent = (
    GameStartEvent
    | GameFinishEvent
    | ChallengeEvent
    | ChallengeCanceledEvent
    | ChallengeDeclinedEvent
)


type BotGameStreamEvent = GameFullEvent | GameStateEvent | ChatLineEvent | OpponentGoneEvent


# Base URL for the API
API_URL = "https://lichess.org"

logger = logging.getLogger(__name__)


class LichessClient:
    """
    Lichess Client

    :param token: Lichess Personal API access token,
                  obtained from https://lichess.org/account/oauth/token
    :type token: `str`
    """

    def __init__(self, token: str, base_url: str = API_URL):
        self.token: str = token
        self.session: TokenSession = TokenSession(token)
        self._requestor = Requestor(self.session, base_url or API_URL, default_fmt=JSON)

    class ApiStream(BaseModel):
        event: ApiStreamEvent

    def stream_incoming_events(self) -> Iterable[ApiStreamEvent]:
        """
        Get your realtime stream of incoming events.
        See https://lichess.org/api#tag/Bot/operation/apiStreamEvent

        :return: stream of incoming events
        """
        path = "/api/stream/event"

        events = self._requestor.get(path, stream=True)

        for event in events:
            logger.debug(f"Raw incoming event: {event}")
            yield self.ApiStream.model_validate({"event": event}).event

    class BotGameStream(BaseModel):
        event: BotGameStreamEvent

    def stream_bot_game_state(self, game_id: str) -> Iterable[BotGameStreamEvent]:
        """
        Get the stream of events for a bot game.
        See https://lichess.org/api#tag/Bot/operation/botGameStream

        :param game_id: ID of a game
        :type game_id: `str`
        :return: iterator over game states
        """
        path = f"/api/bot/game/stream/{game_id}"

        events = self._requestor.get(path, stream=True)

        for event in events:
            yield self.BotGameStream.model_validate({"event": event}).event

    def accept_challenge(self, challenge_id: str):
        """Accept an incoming challenge.

        :param challenge_id: ID of a challenge
        :type challenge_id: `str`
        """
        path = f"/api/challenge/{challenge_id}/accept"

        self._requestor.post(path)

    def decline_challenge(
        self,
        challenge_id: str,
        reason: Literal[
            "generic",
            "later",
            "tooFast",
            "tooSlow",
            "timeControl",
            "rated",
            "casual",
            "standard",
            "variant",
            "noBot",
            "onlyBot",
        ] = "generic",
    ):
        """Decline an incoming challenge.

        :param challenge_id: ID of a challenge
        :param reason: reason for declining challenge
        """
        path = f"/api/challenge/{challenge_id}/decline"
        payload = {"reason": reason}

        self._requestor.post(path, json=payload)

    def bot_write_game_chat_message(
        self, game_id: str, room: Literal["player", "spectator"], text: str
    ):
        """Post a message in a bot game.

        :param game_id: ID of a game
        :type game_id: `str`
        :param room: "player" or "spectator"
        :param text: text of the message
        :type text: `str`
        """
        path = f"/api/bot/game/{game_id}/chat"

        payload = {"room": room, "text": text}

        self._requestor.post(path, json=payload)

    def make_bot_move(self, game_id: str, move: str):
        """Make a move in a bot game.

        :param game_id: ID of a game
        :type game_id: `str`
        :param move: The move to play, in UCI format
        """
        path = f"/api/bot/game/{game_id}/move/{move}"

        self._requestor.post(path)
