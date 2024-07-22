from typing import Annotated

from fastapi import Depends

from libs.gateway.lib import SupplierGatewayApp
from libs.gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    CabinType,
    Rate,
    RatePricing,
    RateRefundPolicy,
)
from libs.gateway.lib.schemas import (
    BaseGetCabinGradePricingData,
    BaseGetCabinGradesData,
    BaseGetRatePricingData,
    BaseGetRatesData,
)


class MSCGatewayApp(SupplierGatewayApp):
    def __init__(self) -> None:
        super().__init__(supplier_name="MSC")

    async def get_rates(
        self, data: Annotated[BaseGetRatesData, Depends()]
    ) -> list[Rate]:
        return [
            Rate(
                code="MSCSPRING2024",
                name="MSC Spring Sale 2024",
                description=(
                    "Enjoy a 20% discount on all MSC spring 2024 cruises. "
                    "Includes $75 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="MSCWINTER2024",
                name="MSC Winter Wonderland 2024",
                description=(
                    "Save 15% on MSC winter 2024 cruises. "
                    "Includes complimentary spa access and $50 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.REFUNDABLE,
            ),
            Rate(
                code="MSCFAMILY2024",
                name="MSC Family Fun Package 2024",
                description=(
                    "Special rates for families in 2024. "
                    "Includes free kids' activities and $100 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.FULLY_NON_REFUNDABLE,
            ),
        ]

    async def get_rate_pricing(
        self, data: Annotated[BaseGetRatePricingData, Depends()]
    ) -> RatePricing:
        return RatePricing(
            base_price=900.00,
            taxes=135.00,
            fees=40.00,
            total_price=1075.00,
            currency="USD",
        )

    async def get_cabin_grades(
        self, data: Annotated[BaseGetCabinGradesData, Depends()]
    ) -> list[CabinGrade]:
        return [
            CabinGrade(
                code="MSCSPRING2024_INSIDE",
                name="MSC Spring Sale Inside Cabin",
                description=(
                    "Enjoy a 20% discount on an inside cabin for MSC spring 2024 cruises. "
                    "Includes $75 onboard credit per cabin."
                ),
                cabin_type=CabinType.INSIDE,
            ),
            CabinGrade(
                code="MSCWINTER2024_BALCONY",
                name="MSC Winter Wonderland Balcony Cabin",
                description=(
                    "Save 15% on a balcony cabin for MSC winter 2024 cruises. "
                    "Includes complimentary spa access and $50 onboard credit per cabin."
                ),
                cabin_type=CabinType.BALCONY,
            ),
            CabinGrade(
                code="MSCFAMILY2024_OUTSIDE",
                name="MSC Family Fun Outside Cabin",
                description=(
                    "Special rates for families in an outside cabin for 2024 cruises. "
                    "Includes free kids' activities and $100 onboard credit per cabin."
                ),
                cabin_type=CabinType.OUTSIDE,
            ),
        ]

    async def get_cabin_grade_pricing(
        self, data: Annotated[BaseGetCabinGradePricingData, Depends()]
    ) -> CabinGradePricing:
        return CabinGradePricing(
            base_price=700.00,
            taxes=105.00,
            fees=30.00,
            total_price=835.00,
            currency="USD",
        )


app = MSCGatewayApp()

if __name__ == "__main__":
    app.run("apps.msc.app.main:app", port=8002)
