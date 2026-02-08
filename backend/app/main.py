from fastapi import FastAPI
from app.api.sample import router

app = FastAPI(
    title="5G Network Simulator Backend",
    description="Dynamic 5G Spectrum Allocation with Quantum ML",
    version="1.0"
)

app.include_router(router)
