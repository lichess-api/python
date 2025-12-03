from pydantic import BaseModel

from .Team import Team


class TeamPaginatorJson(BaseModel):
    """
    TeamPaginatorJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TeamPaginatorJson.yaml
    """

    currentPage: int
    maxPerPage: int
    currentPageResults: tuple[Team, ...]
    previousPage: int | None
    nextPage: int | None
    nbResults: int
    nbPages: int
