from libs.supplier_gateway.lib import EndpointsHandler
from libs.supplier_gateway.lib.models import Rate, RefundPolicy


class RoyalEndpointsHandler(EndpointsHandler):
    async def get_rates(self, sailing_id: int) -> list[Rate]:
        return [
            Rate(
                code="ROYALSUMMER2024",
                name="Royal Caribbean Summer Blast 2024",
                description=(
                    "Get 30% off on Royal Caribbean summer 2024 cruises. "
                    "Includes complimentary shore excursions and $50 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.FULLY_NON_REFUNDABLE,
            ),
            Rate(
                code="ROYALSPRING2024",
                name="Royal Caribbean Spring Fling 2024",
                description=(
                    "Save 20% on spring 2024 cruises with Royal Caribbean. "
                    "Includes $75 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="ROYALWINTER2024",
                name="Royal Caribbean Winter Escape 2024",
                description=(
                    "Enjoy a 25% discount on winter 2024 cruises with Royal Caribbean. "
                    "Includes complimentary spa access and $100 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.REFUNDABLE,
            ),
        ]
