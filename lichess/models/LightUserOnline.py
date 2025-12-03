from .LightUser import LightUser


class LightUserOnline(LightUser):
    """
    LightUserOnline

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/LightUserOnline.yaml
    """

    online: bool | None = None
