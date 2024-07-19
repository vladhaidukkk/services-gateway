from libs.supplier_gateway.lib import EndpointsHandler
from libs.supplier_gateway.lib.models import Rate, RefundPolicy


class NCLEndpointsHandler(EndpointsHandler):
    async def get_rates(self, sailing_id: int) -> list[Rate]:
        return [
            Rate(
                code="NCLFALL2024",
                name="NCL Fall Special 2024",
                description=(
                    "Save 25% on fall 2024 cruises with NCL. "
                    "Includes free specialty dining and $100 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.REFUNDABLE,
            ),
            Rate(
                code="NCLSUMMER2024",
                name="NCL Summer Savings 2024",
                description=(
                    "Get 20% off on NCL summer 2024 cruises. "
                    "Includes complimentary shore excursions and $75 onboard credit per cabin."
                ),
                refund_policy=RefundPolicy.NON_REFUNDABLE_DEPOSIT,
            ),
            Rate(
                code="NCLHOLIDAY2024",
                name="NCL Holiday Special 2024",
                description=(
                    "Enjoy a 30% discount on holiday 2024 cruises with NCL. "
                    "Includes $100 onboard credit and free WiFi."
                ),
                refund_policy=RefundPolicy.FULLY_NON_REFUNDABLE,
            ),
        ]
