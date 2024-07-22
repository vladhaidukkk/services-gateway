from abc import ABC, abstractmethod
from typing import Annotated, Callable, Literal

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse

from libs.gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
)
from libs.gateway.lib.schemas import (
    BaseGetCabinGradePricingData,
    BaseGetCabinGradesData,
    BaseGetRatePricingData,
    BaseGetRatesData,
)


class GatewayApp(ABC):
    def __init__(self, *, gateway_name: str, endpoints_prefix: str = "") -> None:
        if endpoints_prefix:
            assert endpoints_prefix.startswith(
                "/"
            ), f"Invalid endpoints_prefix: '{endpoints_prefix}'. It must start with a '/' character."

        self.app = FastAPI(title=f"{gateway_name} Gateway API")

        @self.app.get("/", include_in_schema=False)
        def index() -> RedirectResponse:
            return RedirectResponse("/docs")

        self._register_endpoint(
            method="get",
            path=f"{endpoints_prefix}/sailings/{{sailing_id}}/rates",
            response_model=list[Rate],
            handler=self.get_rates,
        )
        self._register_endpoint(
            method="get",
            path=f"{endpoints_prefix}/sailings/{{sailing_id}}/rates/{{rate_code}}/pricing",
            response_model=RatePricing,
            handler=self.get_rate_pricing,
        )
        self._register_endpoint(
            method="get",
            path=f"{endpoints_prefix}/sailings/{{sailing_id}}/rates/{{rate_code}}/cabin-grades",
            response_model=list[CabinGrade],
            handler=self.get_cabin_grades,
        )
        self._register_endpoint(
            method="get",
            path=f"{endpoints_prefix}/sailings/{{sailing_id}}/rates/{{rate_code}}/cabin-grades/{{cabin_grade_code}}/pricing",
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
        configure_endpoint = getattr(self.app, method)
        register_endpoint = configure_endpoint(path, response_model=response_model)
        register_endpoint(handler)

    @abstractmethod
    async def get_rates(
        self, data: Annotated[BaseGetRatesData, Depends()]
    ) -> list[Rate]:
        pass

    @abstractmethod
    async def get_rate_pricing(
        self, data: Annotated[BaseGetRatePricingData, Depends()]
    ) -> RatePricing:
        pass

    @abstractmethod
    async def get_cabin_grades(
        self, data: Annotated[BaseGetCabinGradesData, Depends()]
    ) -> list[CabinGrade]:
        pass

    @abstractmethod
    async def get_cabin_grade_pricing(
        self, data: Annotated[BaseGetCabinGradePricingData, Depends()]
    ) -> CabinGradePricing:
        pass

    @staticmethod
    def run(sg_app_path: str, *, port: int) -> None:
        uvicorn.run(f"{sg_app_path}.app", host="127.0.0.1", port=port, reload=True)
