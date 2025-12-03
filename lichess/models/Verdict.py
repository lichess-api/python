from pydantic import BaseModel


class Verdict(BaseModel):
    """
    Verdict

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Verdict.yaml
    """

    condition: str
    verdict: str
