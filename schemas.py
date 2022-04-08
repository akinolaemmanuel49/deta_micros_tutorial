from pydantic import BaseModel, validator


class UserSchema(BaseModel):
    name: str
    email: str
    age: int

    @validator("name")
    def validate_name(cls, v):
        if ' ' in v:
            return v
        else:
            raise ValueError("Name must contain a space")