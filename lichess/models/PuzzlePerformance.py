from pydantic import BaseModel


class PuzzlePerformance(BaseModel):
    """
    PuzzlePerformance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/PuzzlePerformance.yaml
    """

    firstWins: int
    nb: int
    performance: int
    puzzleRatingAvg: int
    replayWins: int
