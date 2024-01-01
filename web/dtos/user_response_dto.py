from typing import Optional, Iterable
from datetime import datetime
from pydantic import BaseModel


class UserResponseDto(BaseModel):
    userId: Optional[str]
    userName: Optional[str]
    email: Optional[str]
    dateTimeCreated: Optional[datetime]
    dateTimeUpdated: Optional[datetime]

    def validate(self, validation_context) -> Iterable:
        pass
