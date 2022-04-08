import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class SubscriberSchema(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    dob: Optional[datetime.date] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

    @validator("name")
    def validate_name(cls, v):
        if ' ' in v:
            return v
        else:
            raise ValueError("Name must contain a space")