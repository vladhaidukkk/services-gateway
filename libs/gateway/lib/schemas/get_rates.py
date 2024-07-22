from dataclasses import dataclass
from typing import Annotated

from fastapi import Path


@dataclass
class BaseGetRatesData:
    sailing_id: Annotated[str, Path()]
