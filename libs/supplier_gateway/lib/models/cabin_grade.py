from enum import StrEnum, auto

from pydantic import BaseModel


class CabinType(StrEnum):
    INSIDE = auto()
    OUTSIDE = auto()
    BALCONY = auto()
    SUITE = auto()


class CabinGrade(BaseModel):
    code: str
    name: str
    description: str
    cabin_type: CabinType
