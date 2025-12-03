"""
See https://github.com/lichess-org/api/tree/master/doc/specs/schemas
"""

from .ArenaPerf import ArenaPerf
from .ArenaPosition import ArenaPosition
from .ArenaRatingObj import ArenaRatingObj
from .ArenaSheet import ArenaSheet
from .ArenaStatus import ArenaStatus
from .ArenaStatusName import ArenaStatusName
from .ArenaTournament import ArenaTournament
from .ArenaTournamentFull import ArenaTournamentFull
from .ArenaTournamentPlayed import ArenaTournamentPlayed
from .ArenaTournamentPlayer import ArenaTournamentPlayer
from .ArenaTournaments import ArenaTournaments

from .BroadcastByUser import BroadcastByUser
from .BroadcastCustomPoints import BroadcastCustomPoints
from .BroadcastCustomScoring import BroadcastCustomScoring
from .BroadcastGroup import BroadcastGroup
from .BroadcastGroupTour import BroadcastGroupTour
from .BroadcastTop import BroadcastTop
from .BroadcastTour import BroadcastTour

from .ChallengeCanceledEvent import ChallengeCanceledEvent
from .ChallengeDeclinedEvent import ChallengeDeclinedEvent
from .ChallengeDeclinedJson import ChallengeDeclinedJson
from .ChallengeEvent import ChallengeEvent
from .ChallengeJson import ChallengeJson
from .ChallengeOpenJson import ChallengeOpenJson
from .ChallengeStatus import ChallengeStatus
from .ChallengeUser import ChallengeUser

from .ChatLineEvent import ChatLineEvent
from .Clock import Clock
from .CloudEval import CloudEval
from .Count import Count
from .Crosstable import Crosstable
from .Error import Error

from .ExternalEngine import ExternalEngine

from .FIDEPlayer import FIDEPlayer
from .Flair import Flair

from .GameChat import GameChat
from .GameColor import GameColor
from .GameCompat import GameCompat
from .GameEventInfo import GameEventInfo
from .GameEventOpponent import GameEventOpponent
from .GameEventPlayer import GameEventPlayer
from .GameFinishEvent import GameFinishEvent
from .GameFullEvent import GameFullEvent
from .GameJson import GameJson
from .GameMoveAnalysis import GameMoveAnalysis
from .GameSource import GameSource
from .GameStartEvent import GameStartEvent
from .GameStateEvent import GameStateEvent
from .GameStatus import GameStatus
from .GameStatusId import GameStatusId
from .GameStatusName import GameStatusName
from .GameUser import GameUser
from .GameUsers import GameUsers

from .Leaderboard import Leaderboard
from .LightUser import LightUser
from .LightUserOnline import LightUserOnline
from .Move import Move
from .NotFound import NotFound
from .OAuthError import OAuthError
from .Ok import Ok
from .OpponentGoneEvent import OpponentGoneEvent

from .PatronColor import PatronColor

from .Perf import Perf
from .Perfs import Perfs
from .PerfTop10 import PerfTop10
from .PerfType import PerfType

from .PlayTime import PlayTime
from .Profile import Profile

from .PuzzleActivity import PuzzleActivity
from .PuzzleModePerf import PuzzleModePerf
from .PuzzlePerformance import PuzzlePerformance
from .PuzzleRacer import PuzzleRacer
from .PuzzleReplay import PuzzleReplay

from .Simul import Simul
from .Speed import Speed
from .StudyMetadata import StudyMetadata

from .SwissStatus import SwissStatus
from .SwissTournament import SwissTournament
from .SwissUnauthorisedEdit import SwissUnauthorisedEdit

from .TablebaseJson import TablebaseJson

from .Team import Team
from .TeamPaginatorJson import TeamPaginatorJson
from .TeamRequest import TeamRequest
from .TeamRequestWithUser import TeamRequestWithUser

from .TimeControl import TimeControl
from .Title import Title
from .Top10s import Top10s
from .TopUser import TopUser
from .TvGame import TvGame
from .UciVariant import UciVariant

from .User import User
from .UserActivityScore import UserActivityScore
from .UserExtended import UserExtended
from .UserNote import UserNote
from .UserStreamer import UserStreamer

from .Variant import Variant
from .VariantKey import VariantKey
from .Verdict import Verdict
from .Verdicts import Verdicts


__all__ = [
    "ArenaPerf",
    "ArenaPosition",
    "ArenaRatingObj",
    "ArenaSheet",
    "ArenaStatus",
    "ArenaStatusName",
    "ArenaTournament",
    "ArenaTournamentFull",
    "ArenaTournamentPlayed",
    "ArenaTournamentPlayer",
    "ArenaTournaments",
    "BroadcastByUser",
    "BroadcastCustomPoints",
    "BroadcastCustomScoring",
    "BroadcastGroup",
    "BroadcastGroupTour",
    "BroadcastTop",
    "BroadcastTour",
    "ChallengeCanceledEvent",
    "ChallengeDeclinedEvent",
    "ChallengeDeclinedJson",
    "ChallengeEvent",
    "ChallengeJson",
    "ChallengeOpenJson",
    "ChallengeStatus",
    "ChallengeUser",
    "ChatLineEvent",
    "Clock",
    "CloudEval",
    "Count",
    "Crosstable",
    "Error",
    "ExternalEngine",
    "FIDEPlayer",
    "Flair",
    "GameChat",
    "GameColor",
    "GameCompat",
    "GameEventInfo",
    "GameEventOpponent",
    "GameEventPlayer",
    "GameFinishEvent",
    "GameFullEvent",
    "GameJson",
    "GameMoveAnalysis",
    "GameSource",
    "GameStartEvent",
    "GameStateEvent",
    "GameStatus",
    "GameStatusId",
    "GameStatusName",
    "GameUser",
    "GameUsers",
    "Leaderboard",
    "LightUser",
    "LightUserOnline",
    "Move",
    "NotFound",
    "OAuthError",
    "Ok",
    "OpponentGoneEvent",
    "PatronColor",
    "Perf",
    "Perfs",
    "PerfTop10",
    "PerfType",
    "PlayTime",
    "Profile",
    "PuzzleActivity",
    "PuzzleModePerf",
    "PuzzlePerformance",
    "PuzzleRacer",
    "PuzzleReplay",
    "Simul",
    "Speed",
    "StudyMetadata",
    "SwissStatus",
    "SwissTournament",
    "SwissUnauthorisedEdit",
    "TablebaseJson",
    "Team",
    "TeamPaginatorJson",
    "TeamRequest",
    "TeamRequestWithUser",
    "TimeControl",
    "Title",
    "Top10s",
    "TopUser",
    "TvGame",
    "UciVariant",
    "User",
    "UserActivityScore",
    "UserExtended",
    "UserNote",
    "UserStreamer",
    "Variant",
    "VariantKey",
    "Verdict",
    "Verdicts",
]
