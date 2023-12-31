from typing import Optional, Iterable
from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel, validator, ValidationError

class UserResponseDto(BaseModel):
    userId: Optional[str]
    userName: Optional[str]
    email: Optional[str]
    dateTimeCreated: Optional[datetime]
    dateTimeUpdated: Optional[datetime]

    def validate(self, validation_context) -> Iterable:
        pass  
