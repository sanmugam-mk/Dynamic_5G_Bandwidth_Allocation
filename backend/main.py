from fastapi import FastAPI

app = FastAPI()
user_state = {}


@app.get("/shan")
#@app.post("/usage")
def receive_usage(data: dict):
    user_id = data["user_id"]
    demand = data["current_demand"]
    user_state[user_id] = demand
    return {"status": "ok"}
