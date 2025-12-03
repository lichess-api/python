from pydantic import BaseModel


class PuzzleActivityPuzzle(BaseModel):
    fen: str
    id: str
    lastMove: str
    plays: int
    rating: int
    solution: tuple[str, ...]
    themes: tuple[str, ...]


class PuzzleActivity(BaseModel):
    """
    PuzzleActivity

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/PuzzleActivity.yaml
    """

    date: int
    puzzle: PuzzleActivityPuzzle
    win: bool
