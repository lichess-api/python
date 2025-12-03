from typing import Literal, Any

from pydantic import BaseModel, HttpUrl, field_validator


class ThematicPosition(BaseModel):
    eco: str
    name: str
    fen: str
    url: HttpUrl


class CustomPosition(BaseModel):
    name: Literal["Custom position"]
    fen: str


type ArenaPositionUnion = ThematicPosition | CustomPosition


class ArenaPosition(BaseModel):
    """
    ArenaPosition

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaPosition.yaml
    """

    position: ArenaPositionUnion | None = None

    @field_validator("position", mode="before")
    @classmethod
    def parse_position(cls, v: dict[str, Any]):
        if not isinstance(v, dict):  # type: ignore
            return v
        if v.get("name") == "Custom position":
            return CustomPosition(**v)
        # fallback to ThematicPosition
        return ThematicPosition(**v)
