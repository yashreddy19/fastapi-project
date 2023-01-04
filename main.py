from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"name": "yashwant"}


@app.get("/about")
def about():
    return {"key": "value"}
