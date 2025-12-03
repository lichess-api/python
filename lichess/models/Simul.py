from pydantic import BaseModel


class Simul(BaseModel):
    """
    Sumiltaneous

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Simul.yaml
    """

    id: str
    host: object
    name: str
    fullName: str
    variants: object
    isCreated: bool
    isFinished: bool
    isRunning: bool
    nbApplicants: int
    nbPairings: int
    text: str | None = None
    estimatedStartAt: int | None = None
    startedAt: int | None = None
    finishedAt: int | None = None
