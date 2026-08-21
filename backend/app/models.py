from pydantic import BaseModel
from typing import Optional


class ChargebackCreate(BaseModel):
    chargeback_id: str
    transaction_id: str
    order_id: str
    amount: float
    currency: str
    reason: str

    customer_id: str
    previous_chargebacks: int = 0

    payment_status: str
    payment_method: str

    order_status: str
    delivery_date: Optional[str] = None
    otp_verified: bool = False

    refund_requested: bool = False
    refund_amount: float = 0