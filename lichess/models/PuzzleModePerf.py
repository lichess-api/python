from pydantic import BaseModel


class PuzzleModePerf(BaseModel):
    """
    Puzzle mode performance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/PuzzleModePerf.yaml
    """

    runs: int
    score: int
