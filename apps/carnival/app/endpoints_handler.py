from libs.supplier_gateway.lib import EndpointsHandler
from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinType,
    Rate,
    RateRefundPolicy,
)


class CarnivalEndpointsHandler(EndpointsHandler):
    async def get_rates(self, sailing_id: str) -> list[Rate]:
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

    async def get_cabin_grades(
        self, sailing_id: str, rate_code: str
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
