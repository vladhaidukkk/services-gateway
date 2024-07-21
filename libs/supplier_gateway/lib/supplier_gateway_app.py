from abc import ABC, abstractmethod
from typing import Annotated, Callable, Literal

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse

from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
)
from libs.supplier_gateway.lib.schemas import (
    GetCabinGradePricingData,
    GetCabinGradesData,
    GetRatePricingData,
    GetRatesData,
)


class SupplierGatewayApp(ABC):
    def __init__(self, *, supplier_name: str) -> None:
        self.app = FastAPI(title=f"{supplier_name} Supplier Gateway")

        @self.app.get("/", include_in_schema=False)
        def index() -> RedirectResponse:
            return RedirectResponse("/docs")

        self._register_endpoint(
            method="get",
            path="/sailings/{sailing_id}/rates",
            response_model=list[Rate],
            handler=self.get_rates,
        )
        self._register_endpoint(
            method="get",
            path="/sailings/{sailing_id}/rates/{rate_code}/pricing",
            response_model=RatePricing,
            handler=self.get_rate_pricing,
        )
        self._register_endpoint(
            method="get",
            path="/sailings/{sailing_id}/rates/{rate_code}/cabin-grades",
            response_model=list[CabinGrade],
            handler=self.get_cabin_grades,
        )
        self._register_endpoint(
            method="get",
            path="/sailings/{sailing_id}/rates/{rate_code}/cabin-grades/{cabin_grade_code}/pricing",
            response_model=CabinGradePricing,
            handler=self.get_cabin_grade_pricing,
        )

    def _register_endpoint(
        self,
        method: Literal["get", "post", "put", "patch", "delete"],
        path: str,
        response_model: any,
        handler: Callable,
    ) -> None:
        register_endpoint = getattr(self.app, method)
        assign_handler = register_endpoint(path, response_model=response_model)
        assign_handler(handler)

    @abstractmethod
    async def get_rates(self, data: Annotated[GetRatesData, Depends()]) -> list[Rate]:
        pass

    @abstractmethod
    async def get_rate_pricing(
        self, data: Annotated[GetRatePricingData, Depends()]
    ) -> RatePricing:
        pass

    @abstractmethod
    async def get_cabin_grades(
        self, data: Annotated[GetCabinGradesData, Depends()]
    ) -> list[CabinGrade]:
        pass

    @abstractmethod
    async def get_cabin_grade_pricing(
        self, data: Annotated[GetCabinGradePricingData, Depends()]
    ) -> CabinGradePricing:
        pass

    @staticmethod
    def run(sg_app_path: str, *, port: int) -> None:
        uvicorn.run(f"{sg_app_path}.app", host="127.0.0.1", port=port, reload=True)
