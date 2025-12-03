from pydantic import BaseModel


class NonmateVariation(BaseModel):
    cp: int
    moves: str


class MateVariation(BaseModel):
    mate: int
    moves: str


PositionVariation = NonmateVariation | MateVariation


class CloudEval(BaseModel):
    """
    CloudEval

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/CloudEval.yaml
    """

    depth: int
    fen: str
    knodes: int
    pvs: tuple[PositionVariation, ...]
