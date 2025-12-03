from typing import Literal

from .ChallengeJson import ChallengeJson


class ChallengeDeclinedJson(ChallengeJson):
    """
    ChallengeDeclinedJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeDeclinedJson.yaml
    """

    declineReason: str
    declineReasonKey: Literal[
        "generic",
        "later",
        "toofast",
        "tooslow",
        "timecontrol",
        "rated",
        "casual",
        "standard",
        "variant",
        "nobot",
        "onlybot",
    ]
