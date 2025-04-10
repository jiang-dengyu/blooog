import os
from dotenv import load_dotenv

#抓.env資訊
load_dotenv()

class Settings:
  DATABASE_URL: str = os.getenv("DATABASE_URL") 
  DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
