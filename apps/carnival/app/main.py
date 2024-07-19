from libs.supplier_gateway.lib import SupplierGatewayApp

app = SupplierGatewayApp(supplier_name="Carnival")

if __name__ == "__main__":
    app.run("apps.carnival.app.main:app", port=8001)
