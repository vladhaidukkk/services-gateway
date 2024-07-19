import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from libs.supplier_gateway.lib.endpoints_handler import EndpointsHandler
from libs.supplier_gateway.lib.models import Rate


class SupplierGatewayApp:
    def __init__(
        self, *, supplier_name: str, endpoints_handler: EndpointsHandler
    ) -> None:
        self.app = FastAPI(title=f"{supplier_name} Supplier Gateway")

        @self.app.get("/", include_in_schema=False)
        def index() -> RedirectResponse:
            return RedirectResponse("/docs")

        @self.app.get("/rates/{sailing_id}", response_model=list[Rate])
        async def get_rates(sailing_id: int) -> list[Rate]:
            return await endpoints_handler.get_rates(sailing_id=sailing_id)

    @staticmethod
    def run(sg_app_path: str, *, port: int) -> None:
        uvicorn.run(f"{sg_app_path}.app", host="127.0.0.1", port=port, reload=True)
