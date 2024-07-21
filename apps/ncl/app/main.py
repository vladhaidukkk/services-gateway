from typing import Annotated

from fastapi import Depends

from libs.supplier_gateway.lib import SupplierGatewayApp
from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    CabinType,
    Rate,
    RatePricing,
    RateRefundPolicy,
)
from libs.supplier_gateway.lib.schemas import (
    GetCabinGradePricingData,
    GetCabinGradesData,
    GetRatePricingData,
    GetRatesData,
)


class NCLGatewayApp(SupplierGatewayApp):
    def __init__(self) -> None:
        super().__init__(supplier_name="NCL")

    async def get_rates(self, data: Annotated[GetRatesData, Depends()]) -> list[Rate]:
        return [
            Rate(
                code="NCLFALL2024",
                name="NCL Fall Special 2024",
                description=(
                    "Save 25% on fall 2024 cruises with NCL. "
                    "Includes free specialty dining and $100 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.REFUNDABLE,
            ),
            Rate(
                code="NCLSUMMER2024",
                name="NCL Summer Savings 2024",
                description=(
                    "Get 20% off on NCL summer 2024 cruises. "
                    "Includes complimentary shore excursions and $75 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="NCLHOLIDAY2024",
                name="NCL Holiday Special 2024",
                description=(
                    "Enjoy a 30% discount on holiday 2024 cruises with NCL. "
                    "Includes $100 onboard credit and free WiFi."
                ),
                refund_policy=RateRefundPolicy.FULLY_NON_REFUNDABLE,
            ),
        ]

    async def get_rate_pricing(
        self, data: Annotated[GetRatePricingData, Depends()]
    ) -> RatePricing:
        return RatePricing(
            base_price=1100.00,
            taxes=165.00,
            fees=35.00,
            total_price=1300.00,
            currency="USD",
        )

    async def get_cabin_grades(
        self, data: Annotated[GetCabinGradesData, Depends()]
    ) -> list[CabinGrade]:
        return [
            CabinGrade(
                code="NCLFALL2024_INSIDE",
                name="NCL Fall Special Inside Cabin",
                description=(
                    "Save 25% on an inside cabin for fall 2024 cruises with NCL. "
                    "Includes free specialty dining and $100 onboard credit per cabin."
                ),
                cabin_type=CabinType.INSIDE,
            ),
            CabinGrade(
                code="NCLSUMMER2024_BALCONY",
                name="NCL Summer Savings Balcony Cabin",
                description=(
                    "Get 20% off on a balcony cabin for NCL summer 2024 cruises. "
                    "Includes complimentary shore excursions and $75 onboard credit per cabin."
                ),
                cabin_type=CabinType.BALCONY,
            ),
            CabinGrade(
                code="NCLHOLIDAY2024_OUTSIDE",
                name="NCL Holiday Special Outside Cabin",
                description=(
                    "Enjoy a 30% discount on an outside cabin for holiday 2024 cruises with NCL. "
                    "Includes $100 onboard credit and free WiFi."
                ),
                cabin_type=CabinType.OUTSIDE,
            ),
        ]

    async def get_cabin_grade_pricing(
        self, data: Annotated[GetCabinGradePricingData, Depends()]
    ) -> CabinGradePricing:
        return CabinGradePricing(
            base_price=800.00,
            taxes=120.00,
            fees=25.00,
            total_price=945.00,
            currency="USD",
        )


app = NCLGatewayApp()

if __name__ == "__main__":
    app.run("apps.ncl.app.main:app", port=8003)
