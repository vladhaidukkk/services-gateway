from abc import ABC, abstractmethod

from libs.supplier_gateway.lib.models import Rate


class EndpointsHandler(ABC):
    @abstractmethod
    async def get_rates(self, sailing_id: int) -> list[Rate]:
        pass
