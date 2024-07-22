from typing import Annotated

from fastapi import Depends, Request

from apps.gateway.app.schemas import (
    GetCabinGradePricingData,
    GetCabinGradesData,
    GetRatePricingData,
    GetRatesData,
)
from apps.gateway.app.supplier_request_router import route_supplier_request
from libs.gateway.lib import GatewayApp
from libs.gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
)


class SuppliersGatewayApp(GatewayApp):
    def __init__(self) -> None:
        super().__init__(gateway_name="Suppliers", endpoints_prefix="/{supplier_name}")

    async def get_rates(
        self, request: Request, _data: Annotated[GetRatesData, Depends()]
    ) -> list[Rate]:
        return await route_supplier_request(request=request)

    async def get_rate_pricing(
        self, request: Request, _data: Annotated[GetRatePricingData, Depends()]
    ) -> RatePricing:
        return await route_supplier_request(request=request)

    async def get_cabin_grades(
        self, request: Request, _data: Annotated[GetCabinGradesData, Depends()]
    ) -> list[CabinGrade]:
        return await route_supplier_request(request=request)

    async def get_cabin_grade_pricing(
        self, request: Request, _data: Annotated[GetCabinGradePricingData, Depends()]
    ) -> CabinGradePricing:
        return await route_supplier_request(request=request)


app = SuppliersGatewayApp()

if __name__ == "__main__":
    app.run("apps.gateway.app.main:app", port=8000)
