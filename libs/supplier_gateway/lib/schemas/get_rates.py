from dataclasses import dataclass
from typing import Annotated

from fastapi import Path


@dataclass
class GetRatesData:
    sailing_id: Annotated[str, Path()]
