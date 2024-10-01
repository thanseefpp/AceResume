from fastapi import APIRouter


router = APIRouter()


@router.get('/hello')
async def test_function():
    return {"response" : "testing"}