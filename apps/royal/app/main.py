from apps.royal.app.endpoints_handler import RoyalEndpointsHandler
from libs.supplier_gateway.lib import SupplierGatewayApp

app = SupplierGatewayApp(
    supplier_name="Royal Caribbean", endpoints_handler=RoyalEndpointsHandler()
)

if __name__ == "__main__":
    app.run("apps.royal.app.main:app", port=8004)
