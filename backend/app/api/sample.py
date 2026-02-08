from fastapi import APIRouter
from app.database.mongo import usage_collection
from app.database.schemas import AllocationPayload
import struct 

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
    data = []

    for doc in usage_collection.find({}, {"_id": 0}):
        data.append(float(doc["demand_prbs"]))
        data.append(float(doc["allocated_prbs"]))
        data.append(float(doc["remaining_buffer"]))

    # Write binary file (float32)
    with open("gnuradio_input.bin", "wb") as f:
        for value in data:
            f.write(struct.pack("f", value))

    print("Binary file written: gnuradio_input.bin")
    print("Total float values:", len(data))

    return {
        "status": "binary file generated",
        "values_written": len(data)
    }

