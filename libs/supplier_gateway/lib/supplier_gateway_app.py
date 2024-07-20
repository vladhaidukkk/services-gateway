import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from libs.supplier_gateway.lib.endpoints_handler import EndpointsHandler
from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    Rate,
    RatePricing,
)


class SupplierGatewayApp:
    def __init__(
        self, *, supplier_name: str, endpoints_handler: EndpointsHandler
    ) -> None:
        self.app = FastAPI(title=f"{supplier_name} Supplier Gateway")

        @self.app.get("/", include_in_schema=False)
        def index() -> RedirectResponse:
            return RedirectResponse("/docs")

        @self.app.get("/sailings/{sailing_id}/rates", response_model=list[Rate])
        async def get_rates(sailing_id: str) -> list[Rate]:
            return await endpoints_handler.get_rates(sailing_id=sailing_id)

        @self.app.get(
            "/sailings/{sailing_id}/rates/{rate_code}/pricing",
            response_model=RatePricing,
        )
        async def get_rate_pricing(sailing_id: str, rate_code: str) -> RatePricing:
            return await endpoints_handler.get_rate_pricing(
                sailing_id=sailing_id, rate_code=rate_code
            )

        @self.app.get(
            "/sailings/{sailing_id}/rates/{rate_code}/cabin-grades",
            response_model=list[CabinGrade],
        )
        async def get_cabin_grades(sailing_id: str, rate_code: str) -> list[CabinGrade]:
            return await endpoints_handler.get_cabin_grades(
                sailing_id=sailing_id, rate_code=rate_code
            )

        @self.app.get(
            "/sailings/{sailing_id}/rates/{rate_code}/cabin-grades/{cabin_grade_code}/pricing",
            response_model=CabinGradePricing,
        )
        async def get_cabin_grade_pricing(
            sailing_id: str, rate_code: str, cabin_grade_code: str
        ) -> CabinGradePricing:
            return await endpoints_handler.get_cabin_grade_pricing(
                sailing_id=sailing_id,
                rate_code=rate_code,
                cabin_grade_code=cabin_grade_code,
            )

    @staticmethod
    def run(sg_app_path: str, *, port: int) -> None:
        uvicorn.run(f"{sg_app_path}.app", host="127.0.0.1", port=port, reload=True)
