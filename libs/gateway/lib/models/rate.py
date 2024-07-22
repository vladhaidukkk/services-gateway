from enum import StrEnum, auto

from pydantic import BaseModel


class RateRefundPolicy(StrEnum):
    REFUNDABLE = auto()
    NON_REFUNDABLE_DEPOSIT = auto()
    FULLY_NON_REFUNDABLE = auto()


class Rate(BaseModel):
    code: str
    name: str
    description: str
    refund_policy: RateRefundPolicy


class RatePricing(BaseModel):
    base_price: float
    taxes: float
    fees: float
    total_price: float
    currency: str
