"""from typing import Dict
from pydantic import BaseModel

class DemandSchema(BaseModel):
    user_id: str
    demand: float
    timestamp: float

class AllocationSchema(BaseModel):
    allocations: Dict[str, float]
    timestamp: float

class NetworkStateSchema(BaseModel):
    timestamp: float
    users: Dict[str, Dict[str, float]]"""
from pydantic import BaseModel
from typing import Dict

class UserAllocation(BaseModel):
    demand_prbs: int
    allocated_prbs: int
    remaining_buffer: float

class AllocationPayload(BaseModel):
    allocations: Dict[int, UserAllocation]
