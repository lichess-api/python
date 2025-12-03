from pydantic import BaseModel


class OAuthError(BaseModel):
    """
    OAuthError

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/OAuthError.yaml
    """

    error: str
    error_description: str
