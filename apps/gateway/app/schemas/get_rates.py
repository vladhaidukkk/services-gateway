from dataclasses import dataclass
from typing import Annotated

from fastapi import Path

from apps.gateway.app.supplier_name import SupplierName
from libs.gateway.lib.schemas import BaseGetRatesData


@dataclass
class GetRatesData(BaseGetRatesData):
    supplier_name: Annotated[SupplierName, Path()]
