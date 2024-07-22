from dataclasses import dataclass
from typing import Annotated

from fastapi import Path


@dataclass
class BaseGetCabinGradesData:
    sailing_id: Annotated[str, Path()]
    rate_code: Annotated[str, Path()]
