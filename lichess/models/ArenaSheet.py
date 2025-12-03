from pydantic import BaseModel


class ArenaSheet(BaseModel):
    """
    ArenaSheet

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaSheet.yaml
    """

    scores: str
    fire: bool | None = None
