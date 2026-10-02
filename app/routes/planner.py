from fastapi import APIRouter, Request

router=APIRouter(prefix="/plan",tags=["Travel Plan"])

@router.post("/")
async def create_travel_plan():
    """Aggregate Weather,Currency and Places data to create a travel plan"""
    
    return {
        "status":"success",
        "message":"Travel plan created successfully"
    }