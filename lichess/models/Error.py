from pydantic import BaseModel


class Error(BaseModel):
    """
    Error

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Error.yaml
    """

    error: str
