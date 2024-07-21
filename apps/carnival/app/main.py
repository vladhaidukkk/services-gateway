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


class CarnivalGatewayApp(SupplierGatewayApp):
    def __init__(self) -> None:
        super().__init__(supplier_name="Carnival")

    async def get_rates(self, data: Annotated[GetRatesData, Depends()]) -> list[Rate]:
        return [
            Rate(
                code="EARLYBIRD2024",
                name="Early Bird Discount for 2024 Cruises",
                description=(
                    "Book early and save 20% on your 2024 cruise. "
                    "Enjoy additional perks like $50 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="SUMMERSALE2024",
                name="Summer Sale 2024",
                description=(
                    "Get 25% off on all summer 2024 cruises. "
                    "Includes $100 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.REFUNDABLE,
            ),
            Rate(
                code="FAMILYFUN2024",
                name="Family Fun Package 2024",
                description=(
                    "Special rates for families in 2024. "
                    "Includes free kids' activities and $75 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
        ]

    async def get_rate_pricing(
        self, data: Annotated[GetRatePricingData, Depends()]
    ) -> RatePricing:
        return RatePricing(
            base_price=800.00,
            taxes=120.00,
            fees=30.00,
            total_price=950.00,
            currency="USD",
        )

    async def get_cabin_grades(
        self, data: Annotated[GetCabinGradesData, Depends()]
    ) -> list[CabinGrade]:
        return [
            CabinGrade(
                code="EB2024_INSIDE",
                name="Early Bird Inside Cabin",
                description=(
                    "Save 20% on an inside cabin for 2024 cruises. "
                    "Includes $50 onboard credit per cabin."
                ),
                cabin_type=CabinType.INSIDE,
            ),
            CabinGrade(
                code="SS2024_BALCONY",
                name="Summer Sale Balcony Cabin",
                description=(
                    "Get 25% off on a balcony cabin for summer 2024 cruises. "
                    "Includes $100 onboard credit per cabin."
                ),
                cabin_type=CabinType.BALCONY,
            ),
            CabinGrade(
                code="FF2024_OUTSIDE",
                name="Family Fun Outside Cabin",
                description=(
                    "Special rates for families in an outside cabin for 2024 cruises. "
                    "Includes free kids' activities and $75 onboard credit per cabin."
                ),
                cabin_type=CabinType.OUTSIDE,
            ),
        ]

    async def get_cabin_grade_pricing(
        self, data: Annotated[GetCabinGradePricingData, Depends()]
    ) -> CabinGradePricing:
        return CabinGradePricing(
            base_price=700.00,
            taxes=100.00,
            fees=25.00,
            total_price=825.00,
            currency="USD",
        )


app = CarnivalGatewayApp()

if __name__ == "__main__":
    app.run("apps.carnival.app.main:app", port=8001)
