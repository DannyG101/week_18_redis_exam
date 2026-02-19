from fastapi import FastAPI
import uvicorn
import dal


app = FastAPI()

@app.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    results = dal.get_alerts_by_border_and_priority()
    return results

@app.get(" /analytics/top-urgent-zones")
def top_urgent_zones():
    results = dal.get_top_urgent_zones()
    return results

@app.get(" /analytics/distance-distribution")
def distance_distribution():
    results = dal.get_distance_distribution()
    return results

@app.get(" /analytics/low-visibility-high-activity")
def low_visibility_high_activity():
    results = dal.get_low_visibility_high_activity()
    return results

@app.get(" /analytics/hot-zones")
def hot_zones():
    results = dal.get_hot_zones()
    return results