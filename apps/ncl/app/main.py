from apps.ncl.app.endpoints_handler import NCLEndpointsHandler
from libs.supplier_gateway.lib import SupplierGatewayApp

app = SupplierGatewayApp(supplier_name="NCL", endpoints_handler=NCLEndpointsHandler())

if __name__ == "__main__":
    app.run("apps.ncl.app.main:app", port=8003)
