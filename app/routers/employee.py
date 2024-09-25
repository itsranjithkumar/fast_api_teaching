
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/")
def read_employees():
   return {"employees": []}


