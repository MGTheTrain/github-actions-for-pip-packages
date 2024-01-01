from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator

class User(BaseModel):
    userId: Optional[str]
    userName: Optional[str]
    userPassword: Optional[str]
    email: Optional[str]
    dateTimeCreated: Optional[datetime]
    dateTimeUpdated: Optional[datetime]

    @validator("userId")
    def validate_user_id(cls, v):
        if v is None:
            raise ValueError("userId can't be empty")
        return v

    @validator("userName")
    def validate_user_name(cls, v):
        if v is None or len(v) > 50:
            raise ValueError("userName can't be empty or exceed 50 characters")
        return v

    @validator("userPassword")
    def validate_user_password(cls, v):
        if v is None or len(v) < 10:
            raise ValueError(
                "userPassword can't be empty or less than 10 characters")
        return v

    @validator("email")
    def validate_email(cls, v):
        if v is None:
            raise ValueError("email can't be empty")
        return v

    @validator("dateTimeCreated")
    def validate_date_time_created(cls, v):
        if v is None:
            raise ValueError("dateTimeCreated can't be empty")
        return v

    @validator("dateTimeUpdated")
    def validate_date_time_updated(cls, v):
        if v is None:
            raise ValueError("dateTimeUpdated can't be empty")
        return v

    @validator("userPassword")
    def validate_password_complexity(cls, v):
        special_char_count = sum(1 for c in v if not c.isalnum())
        digit_count = sum(1 for c in v if c.isdigit())
        upper_count = sum(1 for c in v if c.isupper())
        lower_count = sum(1 for c in v if c.islower())

        if special_char_count < 4 or digit_count < 2 or upper_count < 2 or lower_count < 2:
            raise ValueError(
                "userPassword does not meet complexity requirements.")
        return v