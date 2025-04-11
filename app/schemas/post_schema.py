from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
  title: str
  content: str
  
class PostCreate(PostBase):
  pass

class PostUpdate(PostBase):
  pass

class PostOut(PostBase):
  id: int

  class config:
    orm_mode = True