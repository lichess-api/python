from pydantic import BaseModel


class StudyMetadata(BaseModel):
    """
    StudyMetadata

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/StudyMetadata.yaml
    """

    id: str
    "The study ID"
    name: str
    "The study name"
    createdAt: int
    "The study creation date"
    updatedAt: int
    "The study last update date"
