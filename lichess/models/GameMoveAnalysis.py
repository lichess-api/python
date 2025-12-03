from typing import Literal

from pydantic import BaseModel


class Judgement(BaseModel):
    name: Literal["Inaccuracy", "Mistake", "Blunder"]
    comment: str


class GameMoveAnalysis(BaseModel):
    """
    GameMoveAnalysis

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameMoveAnalysis.yaml
    """

    eval: int
    "Evaluation in centipawns"
    mate: int
    "Number of moves until forced mate"
    best: str
    "Best move in UCI notation (only if played move was inaccurate)"
    variation: str
    "Best variation in SAN notation (only if played move was inaccurate)"
    judgment: Judgement
    "Judgment annotation (only if played move was inaccurate)"
