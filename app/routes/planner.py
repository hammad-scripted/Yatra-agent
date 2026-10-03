from fastapi import APIRouter, Request

router=APIRouter(prefix="/plan",tags=["Travel Plan"])
from app.models.travel import TravelRequest
@router.post("/")
async def create_travel_plan(request: TravelRequest):
    """Aggregate Weather,Currency and Places data to create a travel plan"""
    
    return {
        "status":"success",
        "message":"Travel plan created successfully"
    }