import httpx
from fastapi import Request

from apps.gateway.app.config import settings
from apps.gateway.app.supplier_name import SupplierName


def construct_supplier_url(request: Request) -> str:
    name_to_base_url_map = {
        SupplierName.CARNIVAL: settings.carnival_base_url,
        SupplierName.MSC: settings.msc_base_url,
        SupplierName.NCL: settings.ncl_base_url,
        SupplierName.ROYAL: settings.royal_base_url,
    }

    supplier_name: SupplierName = request.path_params.get("supplier_name")
    supplier_base_url = name_to_base_url_map[supplier_name]
    uri = request.url.path.removeprefix(f"/{supplier_name}")

    return f"{supplier_base_url}{uri}?{request.url.query}"


async def route_supplier_request(request: Request) -> any:
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=construct_supplier_url(request=request),
            headers=request.headers,
            content=await request.body(),
        )
        return response.json()
