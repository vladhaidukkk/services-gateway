from apps.carnival.app.endpoints_handler import CarnivalEndpointsHandler
from libs.supplier_gateway.lib import SupplierGatewayApp

app = SupplierGatewayApp(
    supplier_name="Carnival", endpoints_handler=CarnivalEndpointsHandler()
)

if __name__ == "__main__":
    app.run("apps.carnival.app.main:app", port=8001)
