from pydantic import BaseModel


class Ok(BaseModel):
    """
    Ok

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Ok.yaml
    """

    ok: bool
