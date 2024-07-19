from enum import StrEnum, auto

from pydantic import BaseModel


class RefundPolicy(StrEnum):
    REFUNDABLE = auto()
    NON_REFUNDABLE_DEPOSIT = auto()
    FULLY_NON_REFUNDABLE = auto()


class Rate(BaseModel):
    code: str
    name: str
    description: str
    refund_policy: RefundPolicy
