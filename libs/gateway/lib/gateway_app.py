from abc import ABC, abstractmethod
from typing import Callable, Literal

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from libs.gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
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
    async def get_rates(self, *args, **kwargs) -> list[Rate]:
        """Rates retrieval endpoint handler.

        This method should be implemented to handle the retrieval of rates.

        Parameters
        ----------
        data : Annotated[BaseGetRatesData, Depends()]
            By specifying this data param or an extended version of it, you get not only a single object with all params
            and payload in it, but also the endpoint documentation will be generated based on it.

        """
        pass

    @abstractmethod
    async def get_rate_pricing(self, *args, **kwargs) -> RatePricing:
        """Rate pricing retrieval endpoint handler.

        This method should be implemented to handle the retrieval of rate pricing.

        Parameters
        ----------
        data : Annotated[BaseGetRatePricingData, Depends()]
            By specifying this data param or an extended version of it, you get not only a single object with all params
            and payload in it, but also the endpoint documentation will be generated based on it.

        """
        pass

    @abstractmethod
    async def get_cabin_grades(self, *args, **kwargs) -> list[CabinGrade]:
        """Cabin grades retrieval endpoint handler.

        This method should be implemented to handle the retrieval of cabin grades.

        Parameters
        ----------
        data : Annotated[BaseGetCabinGradesData, Depends()]
            By specifying this data param or an extended version of it, you get not only a single object with all params
            and payload in it, but also the endpoint documentation will be generated based on it.

        """
        pass

    @abstractmethod
    async def get_cabin_grade_pricing(self, *args, **kwargs) -> CabinGradePricing:
        """Cabin grade pricing retrieval endpoint handler.

        This method should be implemented to handle the retrieval of cabin grade pricing.

        Parameters
        ----------
        data : Annotated[BaseGetCabinGradePricingData, Depends()]
            By specifying this data param or an extended version of it, you get not only a single object with all params
            and payload in it, but also the endpoint documentation will be generated based on it.

        """
        pass

    @staticmethod
    def run(sg_app_path: str, *, port: int) -> None:
        uvicorn.run(f"{sg_app_path}.app", host="127.0.0.1", port=port, reload=True)
