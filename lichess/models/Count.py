from pydantic import BaseModel


class Count(BaseModel):
    """
    Count

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Count.yaml
    """

    all: int
    rated: int
    ai: int
    draw: int
    drawH: int
    loss: int
    lossH: int
    win: int
    winH: int
    bookmark: int
    playing: int
    import_: int
    me: int
