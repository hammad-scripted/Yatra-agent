from fastapi import FastAPI

app = FastAPI(
    title="Yatra Planner API",
    description="Aggregate travel data from multiple sources to provide single platform",
    version="1.0.0",
    docs_url="/docs"
)


@app.get("/")
def root():
    return {
        
        "app":"Yatra Planner API",
        "version":"1.0.0",
        "endpoints":{
            "POST /plan":"Create a travel plan (Aggregated)",
            "GET /plan/stream":"Stream travel plan (Server sent events)",
            "GET /plan/cache-stats":"View Cache stats for travel plan",
            "DELETE /plan/cache":"Clear Cache for travel plan"

        }
    }
