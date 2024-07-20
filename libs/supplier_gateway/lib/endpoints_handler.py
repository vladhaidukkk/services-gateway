from abc import ABC, abstractmethod

from libs.supplier_gateway.lib.models import CabinGrade, Rate


class EndpointsHandler(ABC):
    @abstractmethod
    async def get_rates(self, sailing_id: str) -> list[Rate]:
        pass

    @abstractmethod
    async def get_cabin_grades(
        self, sailing_id: str, rate_code: str
    ) -> list[CabinGrade]:
        pass
