from app.config import TOTAL_SPECTRUM

def proportional_allocator(demands: dict) -> dict:

    total_demand = sum(demands.values())

    if total_demand == 0:
        return {user: 0 for user in demands}

    allocation = {}
    for user, demand in demands.items():
        allocation[user] = round(
            (demand / total_demand) * TOTAL_SPECTRUM, 2
        )

    return allocation
