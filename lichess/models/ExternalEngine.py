from pydantic import BaseModel, Field

from .UciVariant import UciVariant


class ExternalEngine(BaseModel):
    """
    ExternalEngine

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ExternalEngine.yaml
    """

    id: str
    "Unique engine registration ID."
    name: str = Field(min_length=3, max_length=200)
    "Display name of the engine."
    clientSecret: str
    """A secret token that can be used to
    [*request* analysis](#tag/External-engine/operation/apiExternalEngineAnalyse)
    from this external engine."""
    userId: str
    "The user this engine has been registered for."
    maxThreads: int = Field(ge=1, le=65536)
    "Maximum number of available threads."
    maxHash: int = Field(ge=1, le=1048576)
    "Maximum available hash table size, in MiB."
    variants: tuple[UciVariant, ...]
    providerData: str | None = None
    """Arbitrary data that the engine provider can use for identification or bookkeeping.

    Users can read this information, but updating it requires knowing or changing the `providerSecret`.
    """
