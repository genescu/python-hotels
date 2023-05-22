from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional


class Validate(BaseModel):
    adults: int
    kids: Optional[int]
    room_type: str
