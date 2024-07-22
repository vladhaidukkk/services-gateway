from dataclasses import dataclass
from typing import Annotated

from fastapi import Path


@dataclass
class BaseGetCabinGradePricingData:
    sailing_id: Annotated[str, Path()]
    rate_code: Annotated[str, Path()]
    cabin_grade_code: Annotated[str, Path()]
