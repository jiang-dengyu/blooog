from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models
from app.database import SessionLocal
from app.controllers import post_controller
router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
  return post_controller.read_posts(db)
