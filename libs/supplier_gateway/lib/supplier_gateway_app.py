import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


class SupplierGatewayApp:
    def __init__(self, supplier_name: str) -> None:
        self.app = FastAPI(title=f"{supplier_name} Supplier Gateway")

        @self.app.get("/", include_in_schema=False)
        def index() -> RedirectResponse:
            return RedirectResponse("/docs")

    @staticmethod
    def run(sg_app_path: str, *, port: int) -> None:
        uvicorn.run(f"{sg_app_path}.app", host="127.0.0.1", port=port, reload=True)
