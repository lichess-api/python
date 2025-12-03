from pydantic import BaseModel


class SwissUnauthorisedEdit(BaseModel):
    """
    SwissUnauthorisedEdit

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/SwissUnauthorisedEdit.yaml
    """

    error: str
