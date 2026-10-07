Base
from date import date 

class TravelRequest(BaseModel):
    destination: str
    departure_date: date
    return_date: date
    base_currency: str = "INR"
    
    
class TravelPlan(BaseModel):
    destination: str
    departure_date: date
    return_date: date
    
    class Config:
        orm_mode = True
        
        
class TravelResponse(BaseModel):
    status: str
    message: str
    data: TravelPlan
    
    class Config:
        orm_mode = True                             
        