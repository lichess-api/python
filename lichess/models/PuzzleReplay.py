from pydantic import BaseModel


class Replay(BaseModel):
    days: int
    theme: str
    nb: int
    remaining: tuple[str, ...]


class Angle(BaseModel):
    key: str
    name: str
    desc: str


class PuzzleReplay(BaseModel):
    """
    PuzzleReplay

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/PuzzleReplay.yaml
    """

    replay: Replay
    angle: Angle
