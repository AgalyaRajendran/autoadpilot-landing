
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

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
        "total_demand": 4200,
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

@app.post("/api/login")
async def login(email: str = Form(...), password: str = Form(...)):
    if email == "admin@nexmax.com" and password == "password123":
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")