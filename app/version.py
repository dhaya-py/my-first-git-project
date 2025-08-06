from fastapi import FastAPI

app = FastAPI()

@app.get("/version")
def version():
    return {"version : 1.0.1"}