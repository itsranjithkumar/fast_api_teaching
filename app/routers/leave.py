from fastapi import APIRouter


router = APIRouter(prefix="/leaves", tags=["leaves"])


@router.get("/")
async def get_leaves():
    return {"hello": "world"}