from libs.supplier_gateway.lib import SupplierGatewayApp

app = SupplierGatewayApp(supplier_name="Royal Caribbean")

if __name__ == "__main__":
    app.run("apps.royal.app.main:app", port=8004)
