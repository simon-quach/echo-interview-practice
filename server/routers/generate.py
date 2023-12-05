from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def generate():
    return [{"hello": "world"}]
