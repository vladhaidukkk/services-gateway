from abc import ABC

from libs.gateway.lib.gateway_app import GatewayApp


class SupplierGatewayApp(GatewayApp, ABC):
    def __init__(self, *, supplier_name: str) -> None:
        super().__init__(gateway_name=f"{supplier_name} Supplier")
