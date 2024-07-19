from libs.supplier_gateway.lib import SupplierGatewayApp

app = SupplierGatewayApp(supplier_name="NCL")

if __name__ == "__main__":
    app.run("apps.ncl.app.main:app", port=8003)
