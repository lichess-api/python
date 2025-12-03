from typing import Literal, Annotated

from pydantic import BaseModel, Field


class ClockTimeControl(BaseModel):
    type: Literal["clock"]
    limit: int
    increment: int
    show: str
    daysPerTurn: int | None = None


class CorrespondenceTimeControl(BaseModel):
    type: Literal["correspondence"]
    daysPerTurn: int
    limit: int | None = None  # not required here
    increment: int | None = None
    show: str | None = None


class UnlimitedTimeControl(BaseModel):
    type: Literal["unlimited"]
    limit: int | None = None
    increment: int | None = None
    show: str | None = None
    daysPerTurn: int | None = None


type TimeControl = Annotated[
    ClockTimeControl | CorrespondenceTimeControl | UnlimitedTimeControl, Field(discriminator="type")
]

"""
TimeControl

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TimeControl.yaml
"""
