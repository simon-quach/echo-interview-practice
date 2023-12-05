from fastapi import FastAPI

from routers.generate import router as generate_router

app = FastAPI()

app.include_router(generate_router, prefix="/generate")


@app.get("/")
async def root():
    return {"message": "Hello World"}
