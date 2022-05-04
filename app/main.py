from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI"
    return {"message": message}