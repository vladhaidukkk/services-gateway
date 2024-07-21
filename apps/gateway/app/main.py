from enum import StrEnum, auto

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
)

app = FastAPI(title="Suppliers Gateway")


class SupplierName(StrEnum):
    CARNIVAL = auto()
    MSC = auto()
    NCL = auto()
    ROYAL = auto()


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/{supplier_name}/sailings/{sailing_id}/rates", response_model=list[Rate])
async def get_rates(
    request: Request, supplier_name: SupplierName, sailing_id: str
) -> list[Rate]:
    pass


@app.get(
    "/{supplier_name}/sailings/{sailing_id}/rates/{rate_code}/pricing",
    response_model=RatePricing,
)
async def get_rate_pricing(
    request: Request, supplier_name: SupplierName, sailing_id: str, rate_code: str
) -> RatePricing:
    pass


@app.get(
    "/{supplier_name}/sailings/{sailing_id}/rates/{rate_code}/cabin-grades",
    response_model=list[CabinGrade],
)
async def get_cabin_grades(
    request: Request, supplier_name: SupplierName, sailing_id: str, rate_code: str
) -> list[CabinGrade]:
    pass


@app.get(
    "/{supplier_name}/sailings/{sailing_id}/rates/{rate_code}/cabin-grades/{cabin_grade_code}/pricing",
    response_model=CabinGradePricing,
)
async def get_cabin_grade_pricing(
    request: Request,
    supplier_name: SupplierName,
    sailing_id: str,
    rate_code: str,
    cabin_grade_code: str,
) -> CabinGradePricing:
    pass


if __name__ == "__main__":
    uvicorn.run("apps.gateway.app.main:app", host="127.0.0.1", port=8000, reload=True)
