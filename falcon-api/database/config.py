import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path(__file__).parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

user = os.getenv("PG_USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
database = os.getenv("PG_DATABASE")
port = os.getenv("PORT")

# sqlalchemy_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
sqlalchemy_url = f"postgres://{user}:{password}@{host}:{port}/{database}"
print("sqlalchemy_url", sqlalchemy_url)

sqlalchemy_engine = create_engine(sqlalchemy_url)