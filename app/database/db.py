import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

env_path=os.path.join(os.path.dirname(__file__),"..","..",".env")
load_dotenv(env_path)

USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
DATABASE=os.getenv("DATABASE")

DB_URL=(f"mysql+pymysql://{USER}:{quote_plus(PASSWORD)}"f"@{HOST}:{PORT}/{DATABASE}")
Base=declarative_base()

engine=create_engine(DB_URL)
Sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
