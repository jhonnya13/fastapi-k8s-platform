from fastapi import FastAPI

app = FastAPI()

@app.get("/recommend")
def recommend(user_id: int = 1):
    return {
        "user_id": user_id,
        "recommended_tracks": ["track_1", "track_2", "track_33"]
    }