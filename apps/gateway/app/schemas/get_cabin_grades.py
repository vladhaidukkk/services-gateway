from dataclasses import dataclass
from typing import Annotated

from fastapi import Path

from apps.gateway.app.supplier_name import SupplierName
from libs.gateway.lib.schemas import BaseGetCabinGradesData


@dataclass
class GetCabinGradesData(BaseGetCabinGradesData):
    supplier_name: Annotated[SupplierName, Path()]
