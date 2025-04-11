from sqlalchemy.orm import Session
from app import models
from app.schemas.post_schema import PostCreate, PostUpdate

def read_posts(db: Session):
  posts = db.query(models.Post).all()
  return posts

def read_post(post_id: int, db: Session):
  return db.query(models.Post).filter(models.Post.id == post_id).first()

def create_post(post: PostCreate, db: Session):
  new_post = models.Post(**post.model_dump())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

def update_post(post_id: int, post_data: PostUpdate, db: Session ):
  post = db.query(models.Post).filter(models.Post.id == post_id).first()
  if post:
    post.title = post_data.title
    post.content = post_data.content
    db.commit()
    db.refresh(post)
  return post

def delete_post(post_id: int, db: Session ):
  post = db.query(models.Post).filter(models.Post.id == post_id).first()
  if post:
    db.delete(post)
    db.commit()
  return post