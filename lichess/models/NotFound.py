from pydantic import BaseModel


class NotFound(BaseModel):
    """
    NotFound

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/NotFound.yaml
    """

    error: str
