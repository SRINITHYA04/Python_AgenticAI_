from fastapi import FastAPI

app = FastAPI(title="FastAPI Crash course")

@app.get("/")
def root():
    return{"messege":"Hello FastAPI"}

@app.get("/Sri")
def root():
    return{"messege":"Hello Srinithya"}