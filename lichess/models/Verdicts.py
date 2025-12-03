from pydantic import BaseModel

from .Verdict import Verdict


class Verdicts(BaseModel):
    """
    Verdicts

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Verdicts.yaml
    """

    accepted: bool
    list: tuple[Verdict, ...]
