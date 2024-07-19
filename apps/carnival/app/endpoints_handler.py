from libs.supplier_gateway.lib import EndpointsHandler
from libs.supplier_gateway.lib.models import Rate, RefundPolicy


class CarnivalEndpointsHandler(EndpointsHandler):
    async def get_rates(self, sailing_id: int) -> list[Rate]:
        return [
            Rate(
                code="EARLYBIRD2024",
                name="Early Bird Discount for 2024 Cruises",
                description=(
                    "Book early and save 20% on your 2024 cruise. "
                    "Enjoy additional perks like $50 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="SUMMERSALE2024",
                name="Summer Sale 2024",
                description=(
                    "Get 25% off on all summer 2024 cruises. "
                    "Includes $100 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.REFUNDABLE,
            ),
            Rate(
                code="FAMILYFUN2024",
                name="Family Fun Package 2024",
                description=(
                    "Special rates for families in 2024. "
                    "Includes free kids' activities and $75 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
        ]
