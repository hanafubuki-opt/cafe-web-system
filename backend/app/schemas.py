from pydantic import BaseModel, EmailStr, ConfigDict

# -------- Users --------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass  # якщо пароль не потрібен — нічого не додаємо

class UserOut(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Можна використати цей тип у списках відповідей
User = UserOut
