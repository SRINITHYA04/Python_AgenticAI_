from fastapi import FastAPI

app = FastAPI(title="FastAPI Crash course")

@app.get("/")
def root():
    return{"messege":"Hello FastAPI"}

@app.get("/Sri")
def root():
    return{"messege":"Hello Srinithya"}

# sending single parameter
@app.get("/users/{user_id}")
def user_name(user_id:int):
    return{"user_id":user_id, "type":str(type(user_id))}

# sending multiple parameter

@app.get("/search")
def search(q: str, page: int=1, limit: int=10):
    return{"q":q, "page": page, "limit":limit}