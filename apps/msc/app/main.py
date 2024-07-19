from libs.supplier_gateway.lib import SupplierGatewayApp

app = SupplierGatewayApp(supplier_name="MSC")

if __name__ == "__main__":
    app.run("apps.msc.app.main:app", port=8002)
