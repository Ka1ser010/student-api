

from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional


class StudentBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    level: str
    active: bool = True


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    level: Optional[str] = None
    active: Optional[bool] = None


class StudentOut(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
