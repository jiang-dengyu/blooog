from sqlalchemy.orm import Session
from app import models

def read_posts(db = Session):
  posts = db.query(models.Post).all()
  return posts