from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"name": "yashwant"}


@app.get("/about")
def about():
    return {"key": "value"}


@app.get("/blog/{id}")
def blog(id: int):
    return {"data": id}
