from pydantic import BaseModel
from typing import Optional

class ReservationBase(BaseModel):
    client_id: str
    entry_date: str
    exit_date: str
    state: str = "confirmada"
    confirmation_code: Optional[str] = None
    channel: Optional[str] = "Web"
    total_amount: Optional[int] = 0
    discount_Id: Optional[str] = None
    observations: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ReservationCreate(ReservationBase):
    pass