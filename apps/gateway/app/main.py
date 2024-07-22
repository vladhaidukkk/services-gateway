from typing import Annotated

import httpx
from fastapi import Depends, Request

from apps.gateway.app.config import settings
from apps.gateway.app.schemas import (
    GetCabinGradePricingData,
    GetCabinGradesData,
    GetRatePricingData,
    GetRatesData,
)
from apps.gateway.app.supplier_name import SupplierName
from libs.gateway.lib import GatewayApp
from libs.gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
)


async def route_supplier_request(request: Request) -> any:
    supplier_name: SupplierName = request.path_params.get("supplier_name")

    if supplier_name == SupplierName.CARNIVAL:
        supplier_base_url = settings.carnival_base_url
    elif supplier_name == SupplierName.MSC:
        supplier_base_url = settings.msc_base_url
    elif supplier_name == SupplierName.NCL:
        supplier_base_url = settings.ncl_base_url
    else:
        supplier_base_url = settings.royal_base_url

    uri = request.url.path.removeprefix(f"/{supplier_name}")
    supplier_url = f"{supplier_base_url}{uri}?{request.url.query}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=supplier_url,
            headers=request.headers,
            content=await request.body(),
        )
        return response.json()


class SuppliersGatewayApp(GatewayApp):
    def __init__(self) -> None:
        super().__init__(gateway_name="Suppliers", endpoints_prefix="/{supplier_name}")

    async def get_rates(
        self, request: Request, data: Annotated[GetRatesData, Depends()]
    ) -> list[Rate]:
        return await route_supplier_request(request=request)

    async def get_rate_pricing(
        self, request: Request, data: Annotated[GetRatePricingData, Depends()]
    ) -> RatePricing:
        return await route_supplier_request(request=request)

    async def get_cabin_grades(
        self, request: Request, data: Annotated[GetCabinGradesData, Depends()]
    ) -> list[CabinGrade]:
        return await route_supplier_request(request=request)

    async def get_cabin_grade_pricing(
        self, request: Request, data: Annotated[GetCabinGradePricingData, Depends()]
    ) -> CabinGradePricing:
        return await route_supplier_request(request=request)


app = SuppliersGatewayApp()

if __name__ == "__main__":
    app.run("apps.gateway.app.main:app", port=8000)
