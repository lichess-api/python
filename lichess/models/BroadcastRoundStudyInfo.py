from pydantic import BaseModel


class BroadcastRoundStudyInfoFeatures(BaseModel):
    chat: bool
    "Whether chat is enabled for the currently authenticated user"
    computer: bool
    "Whether engine analysis is enabled for the currently authenticated user"
    explorer: bool
    "Whether the opening explorer + tablebase is enabled for the currently authenticated user"


class BroadcastRoundStudyInfo(BaseModel):
    """
    BroadcastRoundStudyInfo

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastRoundStudyInfo.yaml
    """

    writeable: bool
    "Whether the currently authenticated user has permission to update the study"
    features: BroadcastRoundStudyInfoFeatures
