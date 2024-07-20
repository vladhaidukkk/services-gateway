from libs.supplier_gateway.lib import EndpointsHandler
from libs.supplier_gateway.lib.models import (
    CabinGrade,
    CabinType,
    Rate,
    RateRefundPolicy,
)


class MSCEndpointsHandler(EndpointsHandler):
    async def get_rates(self, sailing_id: str) -> list[Rate]:
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

    async def get_cabin_grades(
        self, sailing_id: str, rate_code: str
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
