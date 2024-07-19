from libs.supplier_gateway.lib import EndpointsHandler
from libs.supplier_gateway.lib.models import Rate, RefundPolicy


class MSCEndpointsHandler(EndpointsHandler):
    async def get_rates(self, sailing_id: int) -> list[Rate]:
        return [
            Rate(
                code="MSCSPRING2024",
                name="MSC Spring Sale 2024",
                description=(
                    "Enjoy a 20% discount on all MSC spring 2024 cruises. "
                    "Includes $75 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="MSCWINTER2024",
                name="MSC Winter Wonderland 2024",
                description=(
                    "Save 15% on MSC winter 2024 cruises. "
                    "Includes complimentary spa access and $50 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.REFUNDABLE,
            ),
            Rate(
                code="MSCFAMILY2024",
                name="MSC Family Fun Package 2024",
                description=(
                    "Special rates for families in 2024. "
                    "Includes free kids' activities and $100 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.FULLY_NON_REFUNDABLE,
            ),
        ]
