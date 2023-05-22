from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional


class Validate(BaseModel):
    name: str
    address: Optional[str]
    classification: Optional[int]
    reviews_points: Optional[int]
    reviews_number: Optional[int]
    description: str
    room_categories: Optional[list]
    alternative_hotels: Optional[list]
