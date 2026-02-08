from fastapi import APIRouter
from app.database.mongo import usage_collection
from app.database.schemas import AllocationPayload

router = APIRouter()


@router.post("/json_output", summary="Receive Allocation")
def receive_allocation(payload: AllocationPayload):
    """
    Receives allocation data from traffic_generator.py
    Stores it in MongoDB
    """

    for user_id, values in payload.allocations.items():
        usage_collection.insert_one({
            "user_id": user_id,
            "demand_prbs": values.demand_prbs,
            "allocated_prbs": values.allocated_prbs,
            "remaining_buffer": values.remaining_buffer
        })

        print(
            f"[RECEIVED] User {user_id} | "
            f"Demand: {values.demand_prbs} | "
            f"Allocated: {values.allocated_prbs} | "
            f"Remaining Buffer: {values.remaining_buffer}"
        )

    return {"status": "allocation stored"}


@router.get("/fetch_for_gnuradio", summary="Fetch For GNURadio")
def fetch_for_gnuradio():
    """
    Fetches latest allocation data from MongoDB
    (For now, prints it in terminal)
    """

    print("\n===== DATA SENT TO GNU RADIO =====")

    for doc in usage_collection.find({}, {"_id": 0}):
        print(doc)

    print("=================================\n")

    return {"status": "data fetched"}

