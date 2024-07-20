from libs.supplier_gateway.lib import EndpointsHandler
from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinGradePricing,
    CabinType,
    Rate,
    RatePricing,
    RateRefundPolicy,
)


class RoyalEndpointsHandler(EndpointsHandler):
    async def get_rates(self, sailing_id: str) -> list[Rate]:
        return [
            Rate(
                code="ROYALSUMMER2024",
                name="Royal Caribbean Summer Blast 2024",
                description=(
                    "Get 30% off on Royal Caribbean summer 2024 cruises. "
                    "Includes complimentary shore excursions and $50 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.FULLY_NON_REFUNDABLE,
            ),
            Rate(
                code="ROYALSPRING2024",
                name="Royal Caribbean Spring Fling 2024",
                description=(
                    "Save 20% on spring 2024 cruises with Royal Caribbean. "
                    "Includes $75 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="ROYALWINTER2024",
                name="Royal Caribbean Winter Escape 2024",
                description=(
                    "Enjoy a 25% discount on winter 2024 cruises with Royal Caribbean. "
                    "Includes complimentary spa access and $100 onboard credit per cabin."
                ),
                refund_policy=RateRefundPolicy.REFUNDABLE,
            ),
        ]

    async def get_rate_pricing(self, sailing_id: str, rate_code: str) -> RatePricing:
        return RatePricing(
            base_price=1200.00,
            taxes=180.00,
            fees=45.00,
            total_price=1425.00,
            currency="USD",
        )

    async def get_cabin_grades(
        self, sailing_id: str, rate_code: str
    ) -> list[CabinGrade]:
        return [
            CabinGrade(
                code="ROYALSUMMER2024_INSIDE",
                name="Royal Caribbean Summer Blast Inside Cabin",
                description=(
                    "Get 30% off on an inside cabin for Royal Caribbean summer 2024 cruises. "
                    "Includes complimentary shore excursions and $50 onboard credit per cabin."
                ),
                cabin_type=CabinType.INSIDE,
            ),
            CabinGrade(
                code="ROYALSPRING2024_BALCONY",
                name="Royal Caribbean Spring Fling Balcony Cabin",
                description=(
                    "Save 20% on a balcony cabin for spring 2024 cruises with Royal Caribbean. "
                    "Includes $75 onboard credit per cabin."
                ),
                cabin_type=CabinType.BALCONY,
            ),
            CabinGrade(
                code="ROYALWINTER2024_OUTSIDE",
                name="Royal Caribbean Winter Escape Outside Cabin",
                description=(
                    "Enjoy a 25% discount on an outside cabin for winter 2024 cruises with Royal Caribbean. "
                    "Includes complimentary spa access and $100 onboard credit per cabin."
                ),
                cabin_type=CabinType.OUTSIDE,
            ),
        ]

    async def get_cabin_grade_pricing(
        self, sailing_id: str, rate_code: str, cabin_grade_code: str
    ) -> CabinGradePricing:
        return CabinGradePricing(
            base_price=950.00,
            taxes=140.00,
            fees=35.00,
            total_price=1125.00,
            currency="USD",
        )
