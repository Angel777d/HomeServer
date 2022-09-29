from fastapi import FastAPI

app = FastAPI()


@app.get("/auth")
async def root():
    return {"message": "Hello World"}


@app.get("/auth/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
