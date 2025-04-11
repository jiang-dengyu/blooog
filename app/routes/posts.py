from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.controllers import post_controller
from app.schemas.post_schema import PostCreate, PostUpdate, PostOut
from typing import List


router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/", response_model = List[PostOut])
def get_post(db: Session = Depends(get_db)):
  return post_controller.read_posts(db)

@router.get("/{post_id}", response_model = PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
  post = post_controller.read_post(post_id, db)
  if not post:
      raise HTTPException(status_code=404, detail="Post not found")
  return post

@router.post("/", response_model = PostOut)
def create(post: PostCreate, db: Session = Depends(get_db)):
  create_post = post_controller.create_post(post, db)
  return create_post

@router.put("/{post_id}", response_model = PostOut)
def update(post_id: int, post_data: PostUpdate, db: Session = Depends(get_db)):
  updated_post = post_controller.update_post(post_id, post_data, db)
  if not updated_post:
      raise HTTPException(status_code=404, detail="Post not found")
  return updated_post

@router.delete("/{post_id}")
def delete(post_id: int, db: Session = Depends(get_db)):
  deleted = post_controller.delete_post(post_id, db)
  if not deleted:
      raise HTTPException(status_code=404, detail="Post not found")
  return {"message": "Post deleted"}