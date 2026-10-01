from fastapi import FastAPI

app = FastAPI(
    title="Yatra agent"
    description="Yatra agent API for travel services"
    version="1.0.0"
    docs_url="/docs"
)


@app.get("/")
def root():
    return {"message": "Hello World"}
