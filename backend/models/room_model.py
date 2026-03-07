from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class RoomBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int = 0
    images: List[str] = []
    main_image: Optional[str] = None
    active: bool = True


class RoomCreate(RoomBase):
    pass


class RoomUpdate(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    images: Optional[List[str]] = None
    main_image: Optional[str] = None
    active: Optional[bool] = None


class RoomResponse(RoomBase):
    id: str
    created_by: str
    updated_by: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None