from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

# ---- Users ----
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# ---- Menu ----
class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemOut(MenuItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# ---- Orders ----
class OrderBase(BaseModel):
    user_id: int
    total: float
    status: str = "pending"

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
