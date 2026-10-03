from pydantic import BaseModel
from datetime import date
class TravelRequest(BaseModel):
    
    destination: str
    departure_date: date
    return_date: date
    base_currency: str="INR"
    
