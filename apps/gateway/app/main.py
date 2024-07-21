import httpx
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from apps.gateway.app.supplier_name import SupplierName
from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
)

app = FastAPI(title="Suppliers Gateway")


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse("/docs")


async def route_supplier_request(request: Request) -> any:
    supplier_name: SupplierName = request.path_params.get("supplier_name")

    if supplier_name == SupplierName.CARNIVAL:
        supplier_base_url = "http://127.0.0.1:8001"
    elif supplier_name == SupplierName.MSC:
        supplier_base_url = "http://127.0.0.1:8002"
    elif supplier_name == SupplierName.NCL:
        supplier_base_url = "http://127.0.0.1:8003"
    else:
        supplier_base_url = "http://127.0.0.1:8004"

    supplier_url = supplier_base_url + request.url.path.removeprefix(
        f"/{supplier_name}/"
    )

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=supplier_url,
            params=request.query_params,
            headers=request.headers,
            content=await request.body(),
        )
        return response.json()


@app.get("/{supplier_name}/sailings/{sailing_id}/rates", response_model=list[Rate])
async def get_rates(
    request: Request, supplier_name: SupplierName, sailing_id: str
) -> list[dict]:
    return await route_supplier_request(request=request)


@app.get(
    "/{supplier_name}/sailings/{sailing_id}/rates/{rate_code}/pricing",
    response_model=RatePricing,
)
async def get_rate_pricing(
    request: Request, supplier_name: SupplierName, sailing_id: str, rate_code: str
) -> dict:
    return await route_supplier_request(request=request)


@app.get(
    "/{supplier_name}/sailings/{sailing_id}/rates/{rate_code}/cabin-grades",
    response_model=list[CabinGrade],
)
async def get_cabin_grades(
    request: Request, supplier_name: SupplierName, sailing_id: str, rate_code: str
) -> list[dict]:
    return await route_supplier_request(request=request)


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
) -> dict:
    return await route_supplier_request(request=request)


if __name__ == "__main__":
    uvicorn.run("apps.gateway.app.main:app", host="127.0.0.1", port=8000, reload=True)
