
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from db import init_db, save_campaign
import json

app = FastAPI()

init_db()

# Allow your frontend site
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5500"]
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/forecast")
async def get_forecast():
    return JSONResponse(content={
        "total_demand": 4400,
        "total_utilization": 3900,
        "predicted_spend": 1250,
        "roi": 3.5,
        "ctr": 2.1
    })

@app.get("/api/campaigns")
async def get_campaigns():
    return JSONResponse(content={
        "adjustments": [
            {"time": "3:00 PM", "region": "Chicago", "bid": "$1.20", "action": "Increased"},
            {"time": "4:00 PM", "region": "NYC", "bid": "$0.80", "action": "Paused - full occupancy"}
        ]
    })
@app.post("/api/optimize")
async def optimize():
    # Simulate running your reinforcement learning & optimization engine
    return {
        "status": "Optimization executed",
        "adjustments": [
            {"time": "5:00 PM", "region": "LA", "bid": "$1.10", "action": "Increased"},
            {"time": "5:00 PM", "region": "Boston", "bid": "$0.90", "action": "Paused - low demand"}
        ]
    }

@app.post("/api/forecast-train")
async def train_forecast():
    # Simulate retraining your forecasting models (Prophet, LSTM, etc.)
    return {"status": "Forecast model retrained successfully"}

@app.post("/api/login")
async def login(email: str = Form(...), password: str = Form(...)):
    if email == "admin@nexmax.com" and password == "password123":
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/api/create-campaign")
async def create_campaign(request: Request):
    data = await request.json()
    print("Received campaign data")
    print(json.dumps(data, indent=4))
    save_campaign(data)
    return {"message": "Campaign saved to database successfully!"}